#!/bin/env python3
# run in Annotations directory

from lxml import etree
import os

resize_tags = ["xmin","ymin","xmax","ymax"]

def show_orphans():
  for i in os.listdir():
    if i.endswith('xml'):
      r = i.split('.')[0]
      if f'{r}.jpg' not in os.listdir('../JPEGImages'):
        print(f'Asset {r}.jpg is missing.')

def get_bad_boxes(print=False):
  bad_boxes = []
  for i in os.listdir():
    if i.endswith('xml'):
      e = etree.parse(i)
      o = e.findall('object')
      for b in o:
        if b.find('bndbox').find('xmin').text == b.find('bndbox').find('xmax').text:
          bad_boxes.append(i)
          break
        if b.find('bndbox').find('ymin').text == b.find('bndbox').find('ymax').text:
          bad_boxes.append(i)
          break
  if print:
    print(bad_boxes)
  return bad_boxes

def del_orphans():
  for i in os.listdir():
    if i.endswith('xml'):
      r = i.split('.')[0]
      if f'{r}.jpg' not in os.listdir('../JPEGImages'):
        os.remove(i)

def del_bad_boxes():
  bad_boxes = get_bad_boxes()
  for i in os.listdir():
    if i in bad_boxes:
      print(i)
      os.remove(i)
      r = f"{i.split('.')[0]}.jpg"
      if r in os.listdir('../JPEGImages'):
        os.remove(f'../JPEGImages/{r}')

del_orphans()
del_bad_boxes()

