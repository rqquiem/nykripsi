-- sinta_layout.lua — tata letak artikel Sinta (PDF + DOCX).
-- Pakai: pandoc --lua-filter=tools/pandoc_filters/sinta_layout.lua
-- Tiga transformasi AST:
--   A. front matter terpusat (masthead -> judul -> penulis -> afiliasi/email/korespondensi)
--   B. div custom-style="Abstract" -> judul ABSTRAK/ABSTRACT terpusat + isi + kata kunci
--   C. kepala bagian level-1 -> "<HURUF BESAR>" (tanpa penomoran; LT6)
-- Filter ini juga mengonsumsi kunci meta Sinta agar pandoc tidak merender
-- blok judul/penulis sendiri.
local FORMAT_LATEX = FORMAT:match("latex") ~= nil

local function mstr(meta, key)
  local v = meta[key]
  if v == nil then return "" end
  return pandoc.utils.stringify(v)
end

local function meta_authors(meta)
  local v = meta.author
  local out = {}
  if v == nil then return out end
  if v.t == "MetaList" then
    for _, item in ipairs(v) do
      local s = pandoc.utils.stringify(item)
      if s ~= "" then out[#out + 1] = s end
    end
  else
    local s = pandoc.utils.stringify(v)
    if s ~= "" then out[1] = s end
  end
  return out
end

local function lines_to_inlines(lines)
  local out = pandoc.Inlines{}
  local first = true
  for _, l in ipairs(lines) do
    if l ~= nil and l ~= "" then
      if not first then out:insert(pandoc.LineBreak()) end
      out:insert(pandoc.Str(l))
      first = false
    end
  end
  return out
end

local function styled_div(style, blocks)
  return pandoc.Div(blocks, pandoc.Attr("", {}, {{"custom-style", style}}))
end

-- A. Front matter -----------------------------------------------------------
local function build_front_matter(meta)
  local journal = mstr(meta, "journal")
  local month = mstr(meta, "month")
  local year = mstr(meta, "year")
  local volume = mstr(meta, "volume")
  local number = mstr(meta, "number")
  local pages = mstr(meta, "pages")
  local issn_p = mstr(meta, "issn_p")
  local issn_e = mstr(meta, "issn_e")
  local doi = mstr(meta, "doi")
  local title = mstr(meta, "title")
  local affiliation = mstr(meta, "affiliation")
  local email = mstr(meta, "email")
  local corresponding = mstr(meta, "corresponding")
  local authors = meta_authors(meta)
  local authors_joined = table.concat(authors, ", ")

  if FORMAT_LATEX then
    local latex = table.concat({
      "\\begin{center}\n",
      "{\\small " .. journal .. " \\\\ " .. month .. " " .. year .. ", Vol. "
        .. volume .. ", No. " .. number .. ", Hal. " .. pages .. " \\\\\n",
      " ISSN(P): " .. issn_p .. "; ISSN(E): " .. issn_e .. " \\\\ DOI: "
        .. doi .. "}\\\\[6pt]\n",
      "{\\bfseries\\large " .. string.upper(title) .. "}\\\\[6pt]\n",
      "{\\normalsize " .. authors_joined .. "}\\\\[4pt]\n",
      "{\\small " .. affiliation .. " \\\\ Email: " .. email .. " \\\\ (*) "
        .. corresponding .. "}\n",
      "\\end{center}",
    })
    return pandoc.Blocks{pandoc.RawBlock("latex", latex)}
  end

  local blocks = pandoc.Blocks{}
  local masthead = lines_to_inlines({
    journal,
    month .. " " .. year .. ", Vol. " .. volume .. ", No. " .. number
      .. ", Hal. " .. pages,
    "ISSN(P): " .. issn_p .. "; ISSN(E): " .. issn_e,
    "DOI: " .. doi,
  })
  if #masthead > 0 then
    blocks:insert(styled_div("SintaMasthead", {pandoc.Para(masthead)}))
  end
  if title ~= "" then
    blocks:insert(styled_div("Title", {pandoc.Para(pandoc.Inlines{pandoc.Str(title)})}))
  end
  if authors_joined ~= "" then
    blocks:insert(styled_div("Author", {pandoc.Para(pandoc.Inlines{pandoc.Str(authors_joined)})}))
  end
  local affil = lines_to_inlines({
    affiliation,
    email ~= "" and ("Email: " .. email) or "",
    corresponding ~= "" and ("(*) " .. corresponding) or "",
  })
  if #affil > 0 then
    blocks:insert(styled_div("SintaAffiliation", {pandoc.Para(affil)}))
  end
  return blocks
end

function Pandoc(doc)
  local fm = build_front_matter(doc.meta)
  if #fm > 0 then
    fm:extend(doc.blocks)
    doc.blocks = fm
  end
  for _, key in ipairs({
    "title", "author", "date", "affiliation", "email", "corresponding",
    "journal", "volume", "number", "pages", "month", "year", "issn_p",
    "issn_e", "doi", "received", "accepted", "published",
  }) do
    doc.meta[key] = nil
  end
  return doc
end

-- B. Abstrak ----------------------------------------------------------------
local function abstract_heading(label)
  if label == "Abstract" then return "ABSTRACT" end
  return "ABSTRAK"
end

function Div(el)
  if el.attributes["custom-style"] ~= "Abstract" then
    return nil
  end
  local first = el.content[1]
  local second = el.content[2]
  if first == nil or first.t ~= "Para" then
    return nil
  end
  local inlines = first.content
  local strong = inlines[1]
  if strong == nil or strong.t ~= "Strong" then
    return nil
  end
  local label = pandoc.utils.stringify(strong)
  local heading = abstract_heading(label)
  -- buang Strong + Space + "—" + Space
  local idx = 2
  if inlines[idx] and inlines[idx].t == "Space" then idx = idx + 1 end
  if inlines[idx] and inlines[idx].t == "Str" and inlines[idx].text == "\u{2014}" then
    idx = idx + 1
  end
  if inlines[idx] and inlines[idx].t == "Space" then idx = idx + 1 end
  local body = pandoc.Inlines{}
  for i = idx, #inlines do body:insert(inlines[i]) end

  if FORMAT_LATEX then
    local out = pandoc.Blocks{
      pandoc.RawBlock("latex",
        "\\begin{center}\\textbf{" .. heading .. "}\\end{center}"),
      pandoc.Para(body),
    }
    if second ~= nil then out:insert(second) end
    return out
  end
  local out = pandoc.Blocks{
    styled_div("AbstractTitle", {pandoc.Para(pandoc.Inlines{pandoc.Str(heading)})}),
    styled_div("Abstract", {pandoc.Para(body)}),
  }
  if second ~= nil then
    out:insert(styled_div("SintaKeywords", {second}))
  end
  return out
end

-- C. Kepala bagian ----------------------------------------------------------
function Header(el)
  if el.level ~= 1 then
    return nil
  end
  local text = pandoc.utils.stringify(el.content):gsub("%s+$", "")
  el.content = pandoc.Inlines{pandoc.Str(string.upper(text))}
  return el
end
