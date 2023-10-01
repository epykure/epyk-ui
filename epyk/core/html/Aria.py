#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from epyk.core.js.primitives import JsBoolean
from epyk.core.js import JsUtils
from epyk.core.py import primitives


class Aria:

    def __init__(self, component: primitives.HtmlModel):
        self.component = component

    def set(self, arias: dict):
        """
        Set multiple aria properties

        :param arias:
        """
        for k, v in arias.items():
            k = k.replace("aria-", "")
            setattr(self, k, v)

    def custom(self, key: str, val):
        """

        :param key: The key definition of the aria
        :param val:
        """
        self.component.attr["aria-%s" % key] = val

    def get(self, key: str, dfl=None):
        """
        Get the value of a custom aria.

        :param key: The key definition of the aria
        :param dfl: The default value
        """
        return self.component.attr.get("aria-%s" % key, dfl)

    def has(self, key: str) -> bool:
        """
        Check is key existing in the component's aria.

        :param key: The key definition of the aria
        """
        return "aria-%s" % key in self.component.attr

    def js_is(self, key: str, value) -> JsBoolean.JsBoolean:
        """
        Check the value of the component's aria on the JavaScript side.
        Returns a Boolean to be used in a JavaScript expression.

        :param key: The key definition of the aria
        :param value: Aria's value - default string
        """
        return JsBoolean.JsBoolean.get("%s.getAttribute('aria-%s') == %s" % (
            self.component.dom.varId, key, JsUtils.jsConvertData(value, None)))

    @property
    def role(self):
        """

        Example of roles
        Roles: button, checkbox, menuitem, menuitemcheckbox, menuitemradio, option, radio, switch, tab or treeitem
        """
        return self.component.attr.get("role", '')

    @role.setter
    def role(self, val):
        self.component.attr["role"] = val

    @property
    def atomic(self) -> bool:
        """
        Indicates whether assistive technologies will present all, or only parts of, the changed region based on the
        change notifications defined by the aria-relevant attribute.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-atomic
        """
        return self.component.attr.get("aria-atomic", 'false') == 'true'

    @atomic.setter
    def atomic(self, flag: bool):
        self.component.attr["aria-atomic"] = json.dumps(flag)

    @property
    def autocomplete(self):
        """
        Indicates whether inputting text could trigger display of one or more predictions of the user's intended value
        for an input and specifies how predictions would be presented if they are made.

        The aria-autocomplete property describes the type of interaction model a textbox, searchbox, or combobox employs
        when dynamically helping users complete text input.
        It distinguishes between two models: the inline model (aria-autocomplete="inline") that presents a value
        completion prediction inside the text input and the list model (aria-autocomplete="list") that presents a
        collection of possible values in a separate element that pops up adjacent to the text input. It is possible
        for an input to offer both models at the same time (aria-autocomplete="both").

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-autocomplete
        """
        return self.component.attr.get("aria-autocomplete", False)

    @autocomplete.setter
    def autocomplete(self, flag):
        if not flag and "aria-autocomplete" in self.component.attr:
            del self.component.attr["aria-autocomplete"]
        else:
            self.component.attr["aria-autocomplete"] = None

    @property
    def busy(self):
        """
        Indicates an element is being modified and that assistive technologies MAY want to wait until the modifications
        are complete before exposing them to the user.

        The default value of aria-busy is false for all elements. When aria-busy is true for an element, assistive
        technologies MAY ignore changes to content owned by that element and then process all changes made during the
        busy period as a single, atomic update when aria-busy becomes false.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-busy
        """
        return self.component.attr.get("aria-busy", 'false') == 'true'

    @busy.setter
    def busy(self, flag: bool):
        self.component.attr["aria-busy"] = json.dumps(flag)

    @property
    def checked(self) -> bool:
        """
        Indicates the current "checked" state of checkboxes, radio buttons, and other widgets. See related aria-pressed and
        aria-selected.

        The aria-checked attribute indicates whether the element is checked (true), unchecked (false), or represents a
        group of other elements that have a mixture of checked and unchecked values (mixed). Most inputs only support
        values of true and false, but the mixed value is supported by certain tri-state inputs such as a checkbox or
        menuitemcheckbox.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-checked
        """
        return self.component.attr.get("aria-checked", 'false') == 'true'

    @checked.setter
    def checked(self, flag: bool):
        self.component.attr["aria-checked"] = json.dumps(flag)

    @property
    def colcount(self):
        """
        Defines the total number of columns in a table, grid, or treegrid. See related aria-colindex.

        If all of the columns are present in the DOM, it is not necessary to set this attribute as the user agent can
        automatically calculate the total number of columns.
        However, if only a portion of the columns is present in the DOM at a given moment, this attribute is needed to
        provide an explicit indication of the number of columns in the full table.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-colcount
        """
        return self.component.attr.get("aria-colcount", 0)

    @colcount.setter
    def colcount(self, num):
        self.component.attr["aria-colcount"] = num

    @property
    def colindex(self):
        """
        Defines an element's column index or position with respect to the total number of columns within a table, grid, or
        treegrid. See related aria-colcount and aria-colspan.

        If all of the columns are present in the DOM, it is not necessary to set this attribute as the user agent can
        automatically calculate the column index of each cell or gridcell.
        However, if only a portion of the columns is present in the DOM at a given moment, this attribute is needed to
        provide an explicit indication of the column of each cell or gridcell with respect to the full table.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-colindex
        """
        return self.component.attr.get("aria-colindex", 0)

    @colindex.setter
    def colindex(self, num):
        self.component.attr["aria-colindex"] = num

    @property
    def colspan(self):
        """
        Defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid. See related
        aria-colindex and aria-rowspan.

        This attribute is intended for cells and gridcells which are not contained in a native table. When defining the
        column span of cells or gridcells in a native table, authors SHOULD use the host language's attribute instead of
        aria-colspan.
        If aria-colspan is used on an element for which the host language provides an equivalent attribute, user agents
        MUST ignore the value of aria-colspan and instead expose the value of the host language's attribute to assistive
        technologies.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-colspan
        """
        return self.component.attr.get("aria-colspan", 0)

    @colspan.setter
    def colspan(self, num):
        self.component.attr["aria-colspan"] = num

    @property
    def controls(self):
        """
        Identifies the element (or elements) whose contents or presence are controlled by the current element.
        See related aria-owns.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-controls
        """
        return self.component.attr.get("aria-controls")

    @controls.setter
    def controls(self, val):
        self.component.attr["aria-controls"] = val

    @property
    def current(self):
        """
        Indicates the element that represents the current item within a container or set of related elements.

        The aria-current attribute is an enumerated type. Any value not included in the list of allowed values SHOULD be
        treated by assistive technologies as if the value true had been provided.
        If the attribute is not present or its value is an empty string or undefined, the default value of false applies
        and the aria-current state MUST NOT be exposed by user agents or assistive technologies.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-current
        """
        return self.component.attr.get("aria-current")

    @current.setter
    def current(self, val):
        self.component.attr["aria-current"] = val

    @property
    def describedby(self):
        """
        Identifies the element (or elements) that describes the object. See related aria-labelledby.

        The aria-labelledby attribute is similar to the aria-describedby in that both reference other elements to calculate
        a text alternative, but a label should be concise, where a description is intended to provide more verbose
        information.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-describedby
        """
        return self.component.attr.get("aria-describedby")

    @describedby.setter
    def describedby(self, val: str):
        self.component.attr["aria-describedby"] = val

    @property
    def details(self):
        """
        Identifies the element that provides a detailed, extended description for the object. See related
        aria-describedby.

        The aria-details attribute references a single element that provides more detailed information than would
        normally be provided by aria-describedby. It enables assistive technologies to make users aware of the
        availability of an extended description as well as navigate to it. Authors SHOULD ensure the element
        referenced by aria-details is visible to all users.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-details
        """
        return self.component.attr.get("aria-details")

    @details.setter
    def details(self, val):
        self.component.attr["aria-details"] = val

    @property
    def disabled(self) -> bool:
        """
        Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable. See related
        aria-hidden and aria-readonly.

        For example, irrelevant options in a radio group may be disabled.
        Disabled elements might not receive focus from the tab order. For some disabled elements, applications might
        choose not to support navigation to descendants.
        In addition to setting the aria-disabled attribute, authors SHOULD change the appearance (grayed out, etc.) to
        indicate that the item has been disabled.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-disabled
        """
        return self.component.attr.get("aria-disabled", 'false') == 'true'

    @disabled.setter
    def disabled(self, flag: bool):
        self.component.attr["aria-disabled"] = json.dumps(flag)

    @property
    def errormessage(self):
        """
        Identifies the element that provides an error message for the object. See related aria-invalid and
        aria-describedby.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-errormessage
        """
        return self.component.attr.get("aria-errormessage")

    @errormessage.setter
    def errormessage(self, val):
        self.component.attr["aria-errormessage"] = val

    @property
    def expanded(self) -> bool:
        """
        Indicates whether the element, or another grouping element it controls, is currently expanded or collapsed.

        For example, this indicates whether a portion of a tree is expanded or collapsed.
        In other instances, this may be applied to page sections to mark expandable and collapsible regions that are
        flexible for managing content density.
        Simplifying the user interface by collapsing sections may improve usability for all, including those with
        cognitive or developmental disabilities.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-expanded
        """
        return self.component.attr.get("aria-expanded", 'false') == 'true'

    @expanded.setter
    def expanded(self, flag: bool):
        self.component.attr["aria-expanded"] = json.dumps(flag)

    @property
    def flowto(self):
        """
        Identifies the next element (or elements) in an alternate reading order of content which, at the user's
        discretion, allows assistive technology to override the general default of reading in document source order.

        When aria-flowto has a single IDREF, it allows assistive technologies to, at the user's request, forego normal
        document reading order and go to the targeted object.
        However, when aria-flowto is provided with multiple IDREFS, assistive technologies SHOULD present the referenced
        elements as path choices.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-flowto
        """
        return self.component.attr.get("aria-flowto")

    @flowto.setter
    def flowto(self, val):
        self.component.attr["aria-flowto"] = val

    @property
    def haspopup(self) -> bool:
        """
        Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered
        by an element.

        A popup element usually appears as a block of content that is on top of other content.
        Authors MUST ensure that the role of the element that serves as the container for the popup content is menu,
        listbox, tree, grid, or dialog, and that the value of aria-haspopup matches the role of the popup container.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-haspopup
        """
        return self.component.attr.get("aria-haspopup", 'false') == 'true'

    @haspopup.setter
    def haspopup(self, flag: bool):
        self.component.attr["aria-haspopup"] = json.dumps(flag)

    @property
    def hidden(self) -> bool:
        """
        Indicates whether the element is exposed to an accessibility API. See related aria-disabled.

        User agents determine an element's hidden status based on whether it is rendered, and the rendering is usually
        controlled by CSS.
        For example, an element whose display property is set to none is not rendered. An element is considered hidden
        if it, or any of its ancestors are not rendered or have their aria-hidden attribute value set to true.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-hidden
        """
        return self.component.attr.get("aria-hidden", 'false') == 'true'

    @hidden.setter
    def hidden(self, flag: bool):
        self.component.attr["aria-hidden"] = json.dumps(flag)

    @property
    def invalid(self) -> bool:
        """
        Indicates the entered value does not conform to the format expected by the application.
        See related aria-errormessage.

        If the value is computed to be invalid or out-of-range, the application author SHOULD set this attribute to
        true. User agents SHOULD inform the user of the error.
        Application authors SHOULD provide suggestions for corrections if they are known.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-invalid
        """
        return self.component.attr.get("aria-invalid", 'false') == 'true'

    @invalid.setter
    def invalid(self, flag: bool):
        self.component.attr["aria-invalid"] = json.dumps(flag)

    @property
    def keyshortcuts(self):
        """
        Indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.

        The value of the aria-keyshortcuts attribute is a space-delimited list of keyboard shortcuts that can be pressed
        to activate a command or textbox widget.
        The keys defined in the shortcuts represent the physical keys pressed and not the actual characters generated.
        Each keyboard shortcut consists of one or more tokens delimited by the plus sign ("+") representing zero or more
        modifier keys and exactly one non-modifier key that must be pressed simultaneously to activate the given
        shortcut.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-keyshortcuts
        """
        return self.component.attr.get("aria-keyshortcuts")

    @keyshortcuts.setter
    def keyshortcuts(self, val):
        self.component.attr["aria-keyshortcuts"] = val

    @property
    def label(self):
        """
        Defines a string value that labels the current element. See related aria-labelledby.

        The purpose of aria-label is the same as that of aria-labelledby.
        It provides the user with a recognizable name of the object.
        The most common accessibility API mapping for a label is the accessible name property.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-label
        """
        return self.component.attr.get("aria-label")

    @label.setter
    def label(self, val):
        self.component.attr["aria-label"] = val

    @property
    def labelledby(self):
        """
        Identifies the element (or elements) that labels the current element. See related aria-describedby.

        The purpose of aria-labelledby is the same as that of aria-label.
        It provides the user with a recognizable name of the object.
        The most common accessibility API mapping for a label is the accessible name property.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-label
        """
        return self.component.attr.get("aria-labelledby")

    @labelledby.setter
    def labelledby(self, val):
        self.component.attr["aria-labelledby"] = val

    @property
    def level(self):
        """
        Defines the hierarchical level of an element within a structure.

        This can be applied inside trees to tree items, to headings inside a document, to nested grids, nested tablists
        and to other structural items that may appear inside a container or participate in an ownership hierarchy.
        The value for aria-level is an integer greater than or equal to 1.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-level
        """
        return self.component.attr.get("aria-level")

    @level.setter
    def level(self, val):
        self.component.attr["aria-level"] = val

    @property
    def live(self):
        """
        Indicates that an element will be updated, and describes the types of updates the user agents, assistive
        technologies, and user can expect from the live region.

        The values of this attribute are expressed in degrees of importance.
        When regions are specified as polite, assistive technologies will notify users of updates but generally do not
        interrupt the current task, and updates take low priority.
        When regions are specified as assertive, assistive technologies will immediately notify the user, and could
        potentially clear the speech queue of previous updates.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-level
        """
        return self.component.attr.get("aria-live")

    @live.setter
    def live(self, val):
        self.component.attr["aria-live"] = val

    @property
    def modal(self):
        """
        Indicates whether an element is modal when displayed.

        The aria-modal attribute is used to indicate that the presence of a "modal" element precludes usage of other
        content on the page. For example, when a modal dialog is displayed, it is expected that the user's interaction is
        limited to the contents of the dialog, until the modal dialog loses focus or is no longer displayed.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-modal
        """
        return self.component.attr.get("aria-modal")

    @modal.setter
    def modal(self, val):
        self.component.attr["aria-modal"] = val

    @property
    def multiline(self) -> bool:
        """
        Indicates whether a text box accepts multiple lines of input or only a single line.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-multiline
        """
        return self.component.attr.get("aria-multiline", 'false') == 'true'

    @multiline.setter
    def multiline(self, flag: bool):
        self.component.attr["aria-multiline"] = json.dumps(flag)

    @property
    def multiselectable(self):
        """
        Indicates that the user may select more than one item from the current selectable descendants.

        Authors SHOULD ensure that selected descendants have the aria-selected attribute set to true, and selectable
        descendant have the aria-selected attribute set to false. Authors SHOULD NOT use the aria-selected attribute on
        descendants that are not selectable.


        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-multiselectable
        """
        return self.component.attr.get("aria-multiselectable", False)

    @multiselectable.setter
    def multiselectable(self, val):
        self.component.attr["aria-multiselectable"] = val

    @property
    def orientation(self):
        """
        Indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-multiselectable
        """
        return self.component.attr.get("aria-orientation")

    @orientation.setter
    def orientation(self, val):
        self.component.attr["aria-orientation"] = val

    @property
    def owns(self):
        """
        Identifies an element (or elements) in order to define a visual, functional, or contextual parent/child
        relationship between DOM elements where the DOM hierarchy cannot be used to represent the relationship.
        See related aria-controls.

        The value of the aria-owns attribute is a space-separated list of IDREFS that reference one or more elements in
        the document by ID. The reason for adding aria-owns is to expose a parent/child contextual relationship to
        assistive technologies that is otherwise impossible to infer from the DOM.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-owns
        """
        return self.component.attr.get("aria-owns")

    @owns.setter
    def owns(self, val):
        self.component.attr["aria-owns"] = val

    @property
    def placeholder(self):
        """
        Defines a short hint (a word or short phrase) intended to aid the user with data entry when the control has no
        value. A hint could be a sample value or a brief description of the expected format.

        Authors SHOULD NOT use aria-placeholder instead of a label as their purposes are different: The label indicates
        what kind of information is expected. The placeholder text is a hint about the expected value. See related aria-
        labelledby and aria-label.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-placeholder
        """
        return self.component.attr.get("aria-placeholder")

    @placeholder.setter
    def placeholder(self, val: str):
        self.component.attr["aria-placeholder"] = val

    @property
    def posinset(self):
        """
        Defines an element's number or position in the current set of listitems or treeitems. Not required if all elements
        in the set are present in the DOM. See related aria-setsize.

        If all items in a set are present in the document structure, it is not necessary to set this attribute, as the user
        agent can automatically calculate the set size and position for each item. However, if only a portion of the set is
        present in the document structure at a given moment, this property is needed to provide an explicit indication of
        an element's position.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-posinset
        """
        return self.component.attr.get("aria-posinset", 0)

    @posinset.setter
    def posinset(self, num):
        self.component.attr["aria-posinset"] = num

    @property
    def pressed(self) -> bool:
        """
        Indicates the current "pressed" state of toggle buttons. See related aria-checked and aria-selected.

        Toggle buttons require a full press-and-release cycle to change their value. Activating it once changes the value
        to true, and activating it another time changes the value back to false. A value of mixed means that the values of
        more than one item controlled by the button do not all share the same value. Examples of mixed-state buttons are
        described in WAI-ARIA Authoring Practices [wai-aria-practices-1.1]. If the attribute is not present, the button is
        not a toggle button.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-pressed
        """
        return self.component.attr.get("aria-pressed", 'false') == 'true'

    @pressed.setter
    def pressed(self, flag: bool):
        self.component.attr["aria-pressed"] = json.dumps(flag)

    @property
    def readonly(self) -> bool:
        """
        Indicates that the element is not editable, but is otherwise operable. See related aria-disabled.

        This means the user can read but not set the value of the widget.
        Readonly elements are relevant to the user, and application authors SHOULD NOT restrict navigation to the element
        or its focusable descendants. Other actions such as copying the value of the element are also supported.
        This is in contrast to disabled elements, to which applications might not allow user navigation to descendants.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-readonly
        """
        return self.component.attr.get("aria-readonly", 'false') == 'true'

    @readonly.setter
    def readonly(self, flag: bool):
        self.component.attr["aria-readonly"] = json.dumps(flag)

    @property
    def relevant(self) -> bool:
        """
        Indicates what notifications the user agent will trigger when the accessibility tree within a live region is
        modified. See related aria-atomic.

        The attribute is represented as a space delimited list of the following values: additions, removals, text; or a
        single catch-all value all.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-relevant
        """
        return self.component.attr.get("aria-relevant", 'false') == 'true'

    @relevant.setter
    def relevant(self, flag: bool):
        self.component.attr["aria-relevant"] = json.dumps(flag)

    @property
    def roledescription(self):
        """
        Defines a human-readable, author-localized description for the role of an element.

        Some assistive technologies, such as screen readers, present the role of an element as part of the user
        experience. Such assistive technologies typically localize the name of the role, and they may customize it as
        well.
        Users of these assistive technologies depend on the presentation of the role name, such as "region," "button,"
        or "slider," for an understanding of the purpose of the element and, if it is a widget, how to interact with it.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-roledescription
        """
        return self.component.attr.get("aria-roledescription")

    @roledescription.setter
    def roledescription(self, val):
        self.component.attr["aria-roledescription"] = val

    @property
    def rowindex(self):
        """
        Defines an element's row index or position with respect to the total number of rows within a table, grid, or
        treegrid. See related aria-rowcount and aria-rowspan.

        If all of the rows are present in the DOM, it is not necessary to set this attribute as the user agent can
        automatically calculate the index of each row. However, if only a portion of the rows is present in the DOM at a
        given moment, this attribute is needed to provide an explicit indication of each row's position with respect to
        the full table.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-rowindex
        """
        return self.component.attr.get("aria-rowindex")

    @rowindex.setter
    def rowindex(self, num):
        self.component.attr["aria-roledescription"] = num

    @property
    def rowspan(self):
        """
        Defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid. See related
        aria-rowindex and aria-colspan.

        This attribute is intended for cells and gridcells which are not contained in a native table. When defining the
        row span of cells or gridcells in a native table, authors SHOULD use the host language's attribute instead of
        aria-rowspan. If aria-rowspan is used on an element for which the host language provides an equivalent attribute,
        user agents MUST ignore the value of aria-rowspan and instead expose the value of the host language's attribute
        to assistive technologies.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-rowspan
        """
        return self.component.attr.get("aria-rowspan")

    @rowspan.setter
    def rowspan(self, num):
        self.component.attr["aria-rowspan"] = num

    @property
    def selected(self) -> bool:
        """
        Indicates the current "selected" state of various widgets. See related aria-checked and aria-pressed.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-selected
        """
        return self.component.attr.get("aria-selected", 'false') == 'true'

    @selected.setter
    def selected(self, flag: bool):
        self.component.attr["aria-selected"] = json.dumps(flag)

    @property
    def setsize(self):
        """
        Defines the number of items in the current set of listitems or treeitems. Not required if all elements in the
        set are present in the DOM. See related aria-posinset.

        This property is marked on the members of a set, not the container element that collects the members of the set.
        To orient the user by saying an element is "item X out of Y," the assistive technologies would use X equal to
        the aria-posinset attribute and Y equal to the aria-setsize attribute.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-setsize
        """
        return self.component.attr.get("aria-setsize")

    @setsize.setter
    def setsize(self, num):
        self.component.attr["aria-setsize"] = num

    @property
    def sort(self) -> bool:
        """
        Defines the maximum allowed value for a range widget.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-sort
        """
        return self.component.attr.get("aria-sort", 'false') == 'true'

    @sort.setter
    def sort(self, flag: bool):
        self.component.attr["aria-sort"] = json.dumps(flag)

    @property
    def valuemin(self):
        """
        Defines the minimum allowed value for a range widget.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-valuemin
        """
        return self.component.attr.get("aria-valuemin")

    @valuemin.setter
    def valuemin(self, num: float):
        self.component.attr["aria-valuemin"] = num

    @property
    def valuemax(self):
        """
        Defines the maximum allowed value for a range widget.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-valuemax
        """
        return self.component.attr.get("aria-valuemax")

    @valuemax.setter
    def valuemax(self, num: float):
        self.component.attr["aria-valuemax"] = num

    @property
    def valuenow(self):
        """
        Defines the current value for a range widget. See related aria-valuetext.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-valuenow
        """
        return self.component.attr.get("aria-valuenow")

    @valuenow.setter
    def valuenow(self, num: float):
        self.component.attr["aria-valuenow"] = num

    @property
    def valuetext(self):
        """
        Defines the human-readable text alternative of aria-valuenow for a range widget.

        Related Pages:

          https://www.w3.org/TR/wai-aria-1.1/#aria-valuetext
        """
        return self.component.attr.get("aria-valuetext")

    @valuetext.setter
    def valuetext(self, text: str):
        self.component.attr["aria-valuetext"] = text
