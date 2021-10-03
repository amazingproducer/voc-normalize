#!/bin/env python3
from lxml import etree
import os
from tqdm import tqdm

output_dir = './annotations-resized/'

resize_tags = ["width","height","xmin","ymin","xmax","ymax"]

os.mkdir('./annotations-resized')

def get_resize_factor(annotation_file):
  a_file = etree.parse(annotation_file)
  width = int(a_file.xpath(f'/annotation/size/width')[0].text)
  height = int(a_file.xpath(f'/annotation/size/height')[0].text)
  if width > height:
#    print(width/300)
    return width/300
#  print(height/300)
  return height/300
  
def show_resize(annotation_file):
  a_file = etree.parse(annotation_file)
  for i in a_file.iter():
    if i.tag in resize_tags:
      if i.tag == 'xmin':
        print(i.getparent().getparent().find('name').text)
      print(f"{i.tag}({i.text}) => {int(int(i.text)/get_resize_factor(annotation_file))}")

def resize_annotation(annotation_file):
  a_file = etree.parse(annotation_file)
  r_factor = get_resize_factor(annotation_file)
  for i in a_file.iter():
    if i.tag in resize_tags:
      i.text = str(round(int(i.text)/r_factor))
  return(a_file)

def write_annotation(annotation_file):
  resize_annotation(annotation_file).write(f'{output_dir}{annotation_file}')

for i in tqdm(desc='resize_annotations', iterable=os.listdir()):
  if i.endswith('.xml'):
    write_annotation(i)

