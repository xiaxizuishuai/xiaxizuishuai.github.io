# -*- coding: utf-8 -*-
import os

images = []
videos = []

for file in sorted(os.listdir("img/shellcarvingimages/")):
    if file.endswith(".mp4"):
        videos.append(file)
    else:
        images.append(file)

content = """---
layout: post
title: "shellcarving"
subtitle: "贝雕艺术与制作"
author: "xiaxizuishuai"
header-style: text
tags:
  - 贝雕
  - 艺术
---

> **视频记录**

"""

for v in videos:
    content += f"<video src=\"{{{{ site.url }}}}img/shellcarvingimages/{v}\" controls=\"controls\" width=\"100%\"></video>\n\n"

content += "> **材料与作品展示**\n\n"

for img in images:
    content += f"![]({{{{ site.url }}}}img/shellcarvingimages/{img})\n\n"

with open("_posts/2026-06-09-shell.md", "w", encoding="utf-8") as f:
    f.write(content)
print("File written successfully.")
