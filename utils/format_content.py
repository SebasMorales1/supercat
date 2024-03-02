def format_content(content: list[str]=[]) -> list[str]:
  formarted = []

  for text in content:
    if text[-1:] == "\n" and text != "\n":
      formarted.append(text[:-1])
      continue
    formarted.append(text)
  print(formarted)
  return formarted