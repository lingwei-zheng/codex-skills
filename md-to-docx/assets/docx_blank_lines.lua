local empty_para = pandoc.RawBlock('openxml', '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr></w:p>')

local function is_body(block)
  return block.t == 'Para' or block.t == 'Plain'
end

local function is_header(block)
  return block.t == 'Header'
end

local function is_visual(block)
  if block.t == 'Table' or block.t == 'Figure' then
    return true
  end

  if block.t == 'Para' or block.t == 'Plain' then
    if #block.content == 1 and block.content[1].t == 'Image' then
      return true
    end
  end

  return false
end

function Pandoc(doc)
  local out = pandoc.List:new()
  local blocks = doc.blocks

  for i = 1, #blocks do
    local current = blocks[i]
    local next_block = blocks[i + 1]
    out:insert(current)

    if next_block ~= nil and is_visual(current) then
      out:insert(empty_para)
    elseif next_block ~= nil and is_body(current) then
      if is_body(next_block) then
        out:insert(empty_para)
      elseif is_header(next_block) then
        out:insert(empty_para)
        if next_block.level == 1 then
          out:insert(empty_para)
        end
      end
    end
  end

  doc.blocks = out
  return doc
end
