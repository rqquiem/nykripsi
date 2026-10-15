-- bilingual.lua — miringkan blok bahasa kedua (mis. EN) saat bahasa utama Indonesia.
-- Pakai: pandoc --lua-filter=tools/pandoc_filters/bilingual.lua
-- Aturan: setiap Div ber-atribut lang=<kedua> (mis. lang=en) dimiringkan isinya,
-- kecuali run Strong (label **Abstract**/**Keywords:**) yang tetap tegak.
-- Bahasa utama dari meta 'bahasa_utama' bila ada, selain itu dibaca dari
-- assets/bahasa/kamus-id.yaml -> bahasa.utama (default "id").

local main_lang = nil
local meta_lang = nil

-- Meta opsional: bahasa_utama (dipakai bila ada dan tidak kosong).
function Meta(m)
  local v = m["bahasa_utama"]
  if v ~= nil then
    local s = pandoc.utils.stringify(v)
    if s ~= "" then meta_lang = s end
  end
  return m
end

local function get_main()
  if meta_lang ~= nil then return meta_lang end
  if main_lang ~= nil then return main_lang end
  local ok, out = pcall(pandoc.pipe, "python3", {
    "-c",
    "import yaml;print((yaml.safe_load(open('assets/bahasa/kamus-id.yaml')) or {}).get('bahasa',{}).get('utama','id'))",
  }, "")
  if ok and out ~= nil then
    out = out:gsub("%s+$", "")
    if out ~= "" then
      main_lang = out
      return main_lang
    end
  end
  main_lang = "id"
  return main_lang
end

-- Miringkan isi satu Paragraf: kumpulkan inline non-Strong, lalu bungkus Emph.
local function italicize(p)
  local out = pandoc.Inlines{}
  local buf = pandoc.Inlines{}
  local function flush()
    if #buf > 0 then
      out:insert(pandoc.Emph(buf))
      buf = pandoc.Inlines{}
    end
  end
  for _, inl in ipairs(p.content) do
    if inl.t == "Strong" then
      flush()
      out:insert(inl)
    else
      buf:insert(inl)
    end
  end
  flush()
  return pandoc.Para(out)
end

function Div(el)
  local lg = el.attributes.lang
  if lg == nil or lg == "" or lg == get_main() then
    return nil
  end
  return el:walk{ Para = italicize }
end
