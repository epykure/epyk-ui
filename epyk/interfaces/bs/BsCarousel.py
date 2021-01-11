
import os


class Carousels(object):

  def __init__(self, context):
    self.context = context

  def slides(self, imgs, active=None):
    """
    Description:
    ------------
    A slideshow component for cycling through elements—images or slides of text—like a carousel.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/carousel/

    Attributes:
    ----------
    :param imgs:
    :param active:
    """
    schema = {"type": 'div', 'class': 'carousel slide', 'css': None, 'children': [
      {"type": 'div', 'class': 'carousel-inner', 'css': None, 'children': []}]}
    for i in imgs:
      path, img = os.path.split(i)
      schema['children'][0]['children'].append({"type": 'div', 'css': None, 'class': 'carousel-item', 'children': [
        {"type": 'img', 'css': None, 'class': 'd-block w-100', 'args': {"image": img, 'path': path}}
      ]})
      if active == img:
        schema['children'][0]['children'][-1]['class'] = 'carousel-item active'
    if active is None:
      schema['children'][0]['children'][0]['class'] = 'carousel-item active'
    comp = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    comp.attr['data-ride'] = 'carousel'
    return comp

  def controls(self, imgs, active=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/carousel/

    Attributes:
    ----------
    :param imgs:
    :param active:
    """
    schema = {"type": 'div', 'ref': 'carouselExampleIndicators', 'class': 'carousel slide', 'css': None, 'children': [
      {"type": 'div', 'class': 'carousel-inner', 'css': None, 'children': []}]}
    for i in imgs:
      path, img = os.path.split(i)
      schema['children'][0]['children'].append({"type": 'div', 'css': None, 'class': 'carousel-item', 'children': [
        {"type": 'img', 'css': None, 'class': 'd-block w-100', 'args': {"image": img, 'path': path}}
      ]})
      if active == img:
        schema['children'][0]['children'][-1]['class'] = 'carousel-item active'
    if active is None:
      schema['children'][0]['children'][0]['class'] = 'carousel-item active'
    schema['children'].append({"type": 'link', 'class': 'carousel-control-prev', 'attrs': {"role": 'button', 'data-slide': 'prev'},
       'args': {"text": '', 'url': '#%(carouselExampleIndicators)s'}, 'children': [
        {"type": 'span', 'class': 'carousel-control-prev-icon', 'arias': {'hidden': True}},
        {"type": 'span', 'class': 'sr-only', 'args': {'text': 'Previous'}},
      ]})
    schema['children'].append(
      {"type": 'link', 'class': 'carousel-control-next', 'attrs': {"role": 'button', 'data-slide': 'next'},
       'args': {"text": '', 'url': '#%(carouselExampleIndicators)s'}, 'children': [
        {"type": 'span', 'class': 'carousel-control-next-icon', 'arias': {'hidden': True}},
        {"type": 'span', 'class': 'sr-only', 'args': {'text': 'Next'}},
      ]})
    comp = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    comp.attr['data-ride'] = 'carousel'
    return comp

  def incator(self, imgs, active=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/carousel/

    Attributes:
    ----------
    :param imgs:
    :param active:
    """
    schema = {"type": 'div', 'ref': 'carouselExampleIndicators', 'class': 'carousel slide', 'css': None, 'children': [
      {"type": 'div', 'class': 'carousel-inner', 'css': None, 'children': []}]}
    indics = {'type': 'ol', 'class': 'carousel-indicators', 'css': None, 'children': []}
    for k, i in enumerate(imgs):
      indics['children'].append({'type': 'item', 'css': None, 'attrs': {"data-target": '#%(carouselExampleIndicators)s', 'data-slide-to': k}})
      path, img = os.path.split(i)
      schema['children'][0]['children'].append({"type": 'div', 'css': None, 'class': 'carousel-item', 'children': [
        {"type": 'img', 'css': None, 'class': 'd-block w-100', 'args': {"image": img, 'path': path}}]})
      if active == img:
        schema['children'][0]['children'][-1]['class'] = 'carousel-item active'
    schema['children'].insert(0, indics)
    if active is None:
      schema['children'][0]['children'][0]['class'] = 'carousel-item active'
    schema['children'].append(
      {"type": 'link', 'class': 'carousel-control-prev', 'attrs': {"role": 'button', 'data-slide': 'prev'},
       'args': {"text": '', 'url': '#%(carouselExampleIndicators)s'}, 'children': [
        {"type": 'span', 'class': 'carousel-control-prev-icon', 'arias': {'hidden': True}},
        {"type": 'span', 'class': 'sr-only', 'args': {'text': 'Previous'}},
      ]})
    schema['children'].append(
      {"type": 'link', 'class': 'carousel-control-next', 'attrs': {"role": 'button', 'data-slide': 'next'},
       'args': {"text": '', 'url': '#%(carouselExampleIndicators)s'}, 'children': [
        {"type": 'span', 'class': 'carousel-control-next-icon', 'arias': {'hidden': True}},
        {"type": 'span', 'class': 'sr-only', 'args': {'text': 'Next'}},
      ]})
    comp = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    comp.attr['data-ride'] = 'carousel'
    return comp
