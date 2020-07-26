#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.css import Defaults as Defaults_css


class Shopping(object):
  def __init__(self, context):
    self.parent = context

  def product(self, content, price, image, rating=None, title=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param content:
    :param price:
    :param image:
    :param rating:
    :param title:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if title is not None:
      if not hasattr(title, 'options'):
        title = self.parent.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
    if not hasattr(image, 'options'):
      split_url = os.path.split(image)
      div.image = self.parent.context.rptObj.ui.img(split_url[1], path=split_url[0])
      div.image.style.css.margin_bottom = 10
      div.add(div.image)
    if not hasattr(content, 'options'):
      content = self.parent.context.rptObj.ui.text(content)
      content.style.css.display = "block"
    div.add(content)
    if rating is not None:
      if not hasattr(rating, 'options'):
        div.ratings = self.parent.context.rptObj.ui.rich.stars(rating)
        div.add(div.ratings)
    if not hasattr(price, 'options'):
      div.price = self.price(price)
      div.add(div.price)
    return div

  def price(self, price, currency="€", align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param price:
    :param currency:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(price, 'options'):
      split_price = str(price).split(".")
      if len(split_price) > 1:
        div.price = self.parent.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.parent.context.rptObj.ui.tags.sup("%s%s" % (self.parent.context.rptObj.py.encode_html(currency), split_price[1]), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      else:
        div.price = self.parent.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.parent.context.rptObj.ui.tags.sup("%s00" % self.parent.context.rptObj.py.encode_html(currency), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      div.add(self.parent.context.rptObj.ui.div([div.price, price_with_dec]))
    else:
      div.price = price
      div.add(div.price)
    return div

  def price_from(self, price, text="from", currency="€", align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """

    :param price:
    :param text:
    :param currency:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    div.label = self.parent.context.rptObj.ui.text(text)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = '-10px'
    div.add(div.label)
    if not hasattr(price, 'options'):
      split_price = str(price).split(".")
      if len(split_price) > 1:
        div.price = self.parent.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.parent.context.rptObj.ui.tags.sup("%s%s" % (self.parent.context.rptObj.py.encode_html(currency), split_price[1]), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      else:
        div.price = self.parent.context.rptObj.ui.texts.number(split_price[0], options={"type_number": 'number'}, width=(None, "px"))
        div.price.style.css.font_size = Defaults_css.font(10)
        price_with_dec = self.parent.context.rptObj.ui.tags.sup("%s00" % self.parent.context.rptObj.py.encode_html(currency), width=(None, "px"))
        price_with_dec.style.css.font_size = Defaults_css.font(4)
      div.add(self.parent.context.rptObj.ui.div([div.price, price_with_dec]))
    else:
      div.price = price
      div.add(div.price)
    return div

  def description(self, text, url, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def order(self, price, quantty, code, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def rating(self, rating, customers, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def review(self, rating, title, comment, author, date, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def delivery(self, date, price=None, icon="", align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    pass

  def availability(self, flag, comment=None, align="left", width=('auto', ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param flag:
    :param comment:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    comp_availability = self.parent.context.rptObj.ui.text("In Stock", align=align, width=width, height=height, options=options, profile=profile)
    if flag:
      comp_availability.style.css.color = self.parent.context.rptObj.theme.success[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "In Stock"
    else:
      comp_availability.style.css.color = self.parent.context.rptObj.theme.danger[1]
      comp_availability.style.css.bold()
      comp_availability._vals = comment or "Not Available"
    return comp_availability
