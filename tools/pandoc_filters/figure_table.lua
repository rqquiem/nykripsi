-- figure_table.lua — caption tabel + substitusi blok diagram menjadi gambar.
-- Pakai: pandoc --lua-filter=tools/pandoc_filters/figure_table.lua
-- Nomor caption ditulis eksplisit; untuk LaTeX/beamer nomor DIBUANG agar
-- \numberwithin tidak menggandakan; untuk docx nomor DIPERTAHANKAN.
local function numprefix(word)
  return "^" .. word .. "%s+[%d%.]+%s+"
end

local function is_caption(p, word)
  if p.t ~= "Para" then return false end
  return pandoc.utils.stringify(p):match(numprefix(word) .. "%S") ~= nil
end

local function exists(path)
  local fh = io.open(path, "rb")
  if fh then fh:close() return true end
  return false
end

local function caption_text(full, word)
  if FORMAT:match("latex") or FORMAT:match("beamer") then
    return (full:gsub(numprefix(word), ""))
  end
  return full
end

function Blocks(blocks)
  local out = pandoc.Blocks{}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    -- Tabel: paragraf caption tepat sebelum Table
    if is_caption(b, "Tabel") and blocks[i + 1] and blocks[i + 1].t == "Table" then
      local tbl = blocks[i + 1]
      local full = pandoc.utils.stringify(b)
      tbl.caption = pandoc.Caption(pandoc.Inlines{pandoc.Str(caption_text(full, "Tabel"))})
      out:insert(tbl)
      i = i + 2
    -- Gambar: blok diagram + paragraf caption 'Gambar ...' sesudahnya
    elseif b.t == "CodeBlock" and (b.classes:includes("mermaid")
        or b.classes:includes("chart") or b.classes:includes("tikz")
        or b.classes:includes("sintesa")) then
      local id = b.identifier
      local path = "assets/figures/" .. id .. ".png"
      local next_cap = nil
      local j = i + 1
      if j <= #blocks and is_caption(blocks[j], "Gambar") then next_cap = j end
      if id ~= "" and exists(path) then
        local cap = id
        if next_cap then
          cap = caption_text(pandoc.utils.stringify(blocks[next_cap]), "Gambar")
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
