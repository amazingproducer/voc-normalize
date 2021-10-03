#!/bin/env python3
from lxml import etree
import os
from tqdm import tqdm

output_dir = './annotations-mended/'

resize_tags = ["width","height","xmin","ymin","xmax","ymax"]

os.mkdir('./annotations-mended')

def mend_annotation(annotation_file):
  a_file = etree.parse(annotation_file)
  for i in a_file.iter():
    if i.tag in resize_tags:
      if i.text == '0':
        i.text = '1'
  return(a_file)

def show_mendable_annotations(annotation_file):
  a_file = etree.parse(annotation_file)
  for i in a_file.iter():
    if i.tag in resize_tags:
      if i.text == '0':
        print(i.getparent().getparent().find('name').text)

def show_mend():
  for i in os.listdir():
    if i.endswith('.xml'):
      show_mendable_annotations(i)

def write_annotation(annotation_file):
  mend_annotation(annotation_file).write(f'{output_dir}{annotation_file}')

for i in tqdm(desc='mend_annotations', iterable=os.listdir()):
  if i.endswith('.xml'):
    write_annotation(i)

