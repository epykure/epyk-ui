from typing import Optional


def sdom_from(component, content: str):
    return '<%(tag)s %(attr)s>%(content)s</%(tag)s>' % {
        'attr': component.get_attrs(css_class_names=component.style.get_classes()), "content": content,
        "tag": component.tag}


def sdom(tag: str, content: str = "", html_code: str = None, attrs: Optional[dict] = None) -> str:
    if attrs is None:
        attrs = {}
    if html_code :
        attrs["id"] = html_code
    return '<%s %s>%s<%s>' % (tag, " ".join(['%s="%s"' % (k, v) for k, v in attrs.items()]), content, tag)
