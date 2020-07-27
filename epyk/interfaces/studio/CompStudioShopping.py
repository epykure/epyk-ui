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

  def price_discount(self):
    pass

  def description(self, text, url, height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Wrapped link component

    Attributes:
    ----------
    :param text: String. The visible text.
    :param url: String. The link URL when click on the link
    :param height: Tuple. The component height
    :param options: Dictionary. The component properties
    :param profile: Boolean. The component profiling flag
    """
    html_link = self.parent.context.rptObj.ui.link(text, url, height=height, options=options, profile=profile)
    html_link.style.css.color = self.parent.context.rptObj.theme.greys[-1]
    return html_link

  def order(self, price, quantity, code, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param price:
    :param quantity:
    :param code:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.parent.context.rptObj.ui.select(width=width, height=height, options=options, profile=profile, align=align)

    return div

  def discount(self, percent, align="left", width=('auto', ''), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Add a discount tag to a component

    Attributes:
    ----------
    :param percent:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    comp_discount = self.parent.context.rptObj.ui.text("-%s%%" % percent, align=align, width=width, height=height, options=options, profile=profile)
    comp_discount.style.css.background_color = self.parent.context.rptObj.theme.danger[1]
    comp_discount.style.css.color = "white"
    comp_discount.style.css.min_width = "30px"
    comp_discount.style.css.bold()
    comp_discount.style.css.padding = "7px 5px"
    comp_discount.style.css.margin = "5px"
    comp_discount.style.css.border_radius = "50%"
    return comp_discount

  def rating(self, rating, customers, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """

    :param rating:
    :param customers:
    :param url:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    container = self.parent.context.rptObj.ui.div([])
    container.stars = self.parent.context.rptObj.ui.rich.stars(rating, best=options.get("stars", 5))
    container.stars.style.display = "inline-block"
    container.stars.style.margin_right = 5
    container.link = self.parent.context.rptObj.ui.link("(%s)" % customers, url)
    container.add(container.stars)
    container.add(container.link)
    return container

  def tags(self, tags, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """

    :param tags:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.parent.context.rptObj.ui.text(tag)
      else:
        comp_tag = tag
      comp_tag.style.css.background = self.parent.context.rptObj.theme.colors[4]
      comp_tag.style.css.color = "white"
      comp_tag.style.css.margin = "0 3px"
      comp_tag.style.css.padding = "1px 5px"
      comp_tag.style.css.border_radius = "20px"
      container.add(comp_tag)
    return container

  def quality(self, votes, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Return a skillbar chart for the customer review ratings

    Attributes:
    ----------
    :param votes: Dictionary. Number of customer review per rating
    :param url: String. Url template for product link to those customer rating comments
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    vote_records = []
    dflt_options = {"unit": '%', "values": True, "background": self.parent.context.rptObj.theme.colors[6], 'borders': True}
    if options is not None:
      dflt_options.update(options)
    customers = sum([k for k in votes.values()])
    for i in reversed(range(dflt_options.get("stars", 5))):
      if url is not None:
        vote_records.append({"star": self.parent.context.rptObj.ui.link("%s stars" % i, url % i), "value":  votes.get(i, 0) / customers * 100})
      else:
        vote_records.append({"star": "%s stars" % i, "value":  votes.get(i, 0) / customers * 100})
    comp = self.parent.context.rptObj.ui.charts.skillbars(vote_records, y_column='value', x_axis='star', options=dflt_options).css({"width": "%s%s" % (width[0], width[1])})
    return comp

  def question(self, rating, customers, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
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
