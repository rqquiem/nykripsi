-- figure_table.lua — caption tabel + substitusi blok diagram menjadi gambar.
-- Pakai: pandoc --lua-filter=tools/pandoc_filters/figure_table.lua
-- Nomor caption ditulis eksplisit; untuk LaTeX/beamer nomor DIBUANG agar
-- \numberwithin tidak menggandakan; untuk docx nomor DIPERTAHANKAN.
local function numprefix(word)
  -- Lua patterns lack '(?:...)' and '|' (unlike regex); expand 'A|B' into
  -- anchored alternatives so both ID (Tabel/Gambar) and EN (Table/Figure) match.
  local pats = {}
  for w in word:gmatch("[^|]+") do
    pats[#pats + 1] = "^" .. w .. "%s+[%d%.]+%s+"
  end
  return pats
end

local function is_caption(p, word)
  if p.t ~= "Para" then return false end
  local s = pandoc.utils.stringify(p)
  for _, pat in ipairs(numprefix(word)) do
    if s:match(pat .. "%S") ~= nil then return true end
  end
  return false
end

local function exists(path)
  local fh = io.open(path, "rb")
  if fh then fh:close() return true end
  return false
end

local function caption_text(full, word)
  if FORMAT:match("latex") or FORMAT:match("beamer") then
    for _, pat in ipairs(numprefix(word)) do
      if full:match(pat .. "%S") ~= nil then return (full:gsub(pat, "")) end
    end
  end
  return full
end

function Blocks(blocks)
  local out = pandoc.Blocks{}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    -- Tabel: paragraf caption tepat sebelum Table
    if is_caption(b, "Tabel|Table") and blocks[i + 1] and blocks[i + 1].t == "Table" then
      local tbl = blocks[i + 1]
      local full = pandoc.utils.stringify(b)
      tbl.caption = pandoc.Caption(pandoc.Inlines{pandoc.Str(caption_text(full, "Tabel|Table"))})
      out:insert(tbl)
      i = i + 2
    -- Gambar: blok diagram + paragraf caption 'Gambar ...' sesudahnya
    elseif b.t == "CodeBlock" and (b.classes:includes("mermaid")
        or b.classes:includes("chart") or b.classes:includes("tikz")
        or b.classes:includes("sintesa") or b.classes:includes("bagan")) then
      local id = b.identifier
      local path = "assets/figures/" .. id .. ".png"
      local next_cap = nil
      local j = i + 1
      if j <= #blocks and is_caption(blocks[j], "Gambar|Figure") then next_cap = j end
      if id ~= "" and exists(path) then
        local cap = id
        if next_cap then
          cap = caption_text(pandoc.utils.stringify(blocks[next_cap]), "Gambar|Figure")
        end
        local img = pandoc.Image({}, path)
        out:insert(pandoc.Figure(
          pandoc.Para{img},
          pandoc.Caption(pandoc.Inlines{pandoc.Str(cap)})))
        i = next_cap and (next_cap + 1) or (i + 1)
      else
        io.stderr:write("figure_table: aset hilang: " .. path .. "\n")
        out:insert(b)
        i = i + 1
      end
    else
      out:insert(b)
      i = i + 1
    end
  end
  return out
end
