-- table.lua — ubah blok ```{.table #tbl-<slug>} (YAML) menjadi tabel native.
-- Pakai: pandoc --lua-filter=tools/pandoc_filters/table.lua
-- Caption diambil dari paragraf 'Tabel <n> <Judul>' tepat di atas blok; untuk
-- LaTeX nomor dibuang (auto-number via \caption), untuk DOCX dipertahankan.
-- Body YAML disalurkan ke tools/table.py --format <latex|docx>.

local function numprefix(word)
  -- Lua patterns lack '(?:...)' and '|' (unlike regex); expand 'A|B' into
  -- anchored alternatives so both ID (Tabel) and EN (Table) match.
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
    if b.t == "CodeBlock" and b.classes:includes("table") then
      local fmt = FORMAT:match("latex") and "latex"
        or (FORMAT:match("docx") and "docx" or nil)
      if fmt == nil then
        out:insert(b)
        i = i + 1
      else
        local cap = ""
        local had_caption = false
        local prev = blocks[i - 1]
        if prev ~= nil and is_caption(prev, "Tabel|Table") then
          had_caption = true
          cap = caption_text(pandoc.utils.stringify(prev), "Tabel|Table")
        end
        local ok, res = pcall(pandoc.pipe, "python3",
          {"tools/table.py", "--format", fmt, "--caption", cap}, b.text)
        if ok then
          -- Caption tepat di atas sudah ter-emit; buang agar hanya tabel tersisa.
          if had_caption and #out > 0 then out:remove(#out) end
          out:insert(pandoc.RawBlock(fmt == "latex" and "latex" or "openxml", res))
          i = i + 1
        else
          io.stderr:write("table: gagal (" .. tostring(res) .. ")\n")
          out:insert(b)
          i = i + 1
        end
      end
    else
      out:insert(b)
      i = i + 1
    end
  end
  return out
end
