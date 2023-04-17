from epyk.core.html.options import Options


class InnerButtons(Options):

    @property
    def text(self):
        """
        Being able to let your users know what will happen when they activate a button is obviously fundamentally important
        to the Buttons extension and this option provides exactly that ability.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.text
        """
        return self._config_get()

    @text.setter
    def text(self, val):
        self._config(val)

    @property
    def action(self):
        """
        This function defined the action that the button will take when activated by the end user.
        This will normally be to perform some operation on the DataTable, but can be absolutely anything since the
        function can be defined by yourself.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.action
        """
        return self._config_get()

    @action.setter
    def action(self, val):
        self._config(val)

    @property
    def attr(self):
        """
        This option provides the ability to set any arbitrary attribute on the button's HTML element in the document.
        This can be useful for customisation of attributes such as ARIA assistive attributes, setting a custom id for
        selection / styling, custom data parameters, etc.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.attr
        """
        return self._config_get()

    @attr.setter
    def attr(self, val):
        self._config(val)

    @property
    def className(self):
        """
        Set the class name for the button.
        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.className
        """
        return self._config_get()

    @className.setter
    def className(self, val):
        self._config(val)

    @property
    def available(self):
        """
        Ensure that any requirements have been satisfied before initialising a button.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.available
        """
        return self._config_get()

    @available.setter
    def available(self, val):
        self._config(val)

    @property
    def enabled(self):
        """
        This option provides the ability to set the initial enabled state of a button using a boolean value.

        It is most likely to be of use when using the API methods that can control the button's enabled state after
        initialisation:

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.enabled
        """
        return self._config_get()

    @enabled.setter
    def enabled(self, val):
        self._config(val)

    @property
    def extend(self):
        """
        Define which button type the button should be based on.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.extend
        """
        return self._config_get()

    @extend.setter
    def extend(self, val):
        self._config(val)

    @property
    def key(self):
        """
        Define an activation key for a button.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.key
        """
        return self._config_get()

    @key.setter
    def key(self, val):
        self._config(val)

    @property
    def name(self):
        """
        Define a name for a button.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.name
        """
        return self._config_get()

    @name.setter
    def name(self, val):
        self._config(val)

    @property
    def tag(self):
        """
        Define a tag  for a button.

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.tag
        """
        return self._config_get()

    @tag.setter
    def tag(self, val):
        self._config(val)

    @property
    def titleAttr(self):
        """
        This option provides the ability to set the title attribute for the button.

        This can be used to provide a detailed description of the button, or a simple text name if you choose to display
        an icon in the button rather than text (using the buttons.buttons.text option).

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.titleAttr
        """
        return self._config_get()

    @titleAttr.setter
    def titleAttr(self, val):
        self._config(val)


class Buttons(Options):
    class Dom(Options):
        class Container(Options):
            @property
            def tag(self):
                return self._config_get()

            @tag.setter
            def tag(self, val):
                self._config(val)

            @property
            def className(self):
                return self._config_get()

            @className.setter
            def className(self, val):
                self._config(val)

        class ButtonLiner(Options):
            @property
            def tag(self):
                return self._config_get()

            @tag.setter
            def tag(self, val):
                self._config(val)

            @property
            def className(self):
                return self._config_get()

            @className.setter
            def className(self, val):
                self._config(val)

        class Collection(Options):
            @property
            def tag(self):
                return self._config_get()

            @tag.setter
            def tag(self, val):
                self._config(val)

            @property
            def className(self):
                return self._config_get()

            @className.setter
            def className(self, val):
                self._config(val)

        class DomButton(Options):
            @property
            def tag(self):
                return self._config_get()

            @tag.setter
            def tag(self, val):
                self._config(val)

            @property
            def className(self):
                return self._config_get()

            @className.setter
            def className(self, val):
                self._config(val)

            @property
            def disabled(self):
                return self._config_get()

            @disabled.setter
            def disabled(self, val):
                self._config(val)

            @property
            def active(self):
                return self._config_get()

            @active.setter
            def active(self, val):
                self._config(val)

        @property
        def buttonContainer(self):
            """
            This option provides the ability for each button to be wrapped in another element.
            This can be useful for cases where the styling framework requires a list of buttons,
            where the list element is just a container and not the button itself (Zurb Foundation requires this for example).

            Related Pages:

               https://datatables.net/reference/option/buttons.buttons.buttonContainer
            """
            return self._config_sub_data('buttonContainer', self.Container)

        @property
        def buttonLiner(self):
            """
            This option controls the HTML tag that is used as the liner for each button.
            This can be particularly useful for adding complex styling rules to buttons.
            It can also be disabled if you wish to have minimal markup in your document.

            Related Pages:

              https://datatables.net/reference/option/buttons.buttons.buttonLiner
            """
            return self._config_sub_data('buttonLiner', self.ButtonLiner)

        @property
        def collection(self):
            """
            This option controls the HTML tag that is used for the element that is displayed when a collection button is
            triggered. It in turn contains the sub-buttons of the collection.

            Related Pages:

              https://datatables.net/reference/option/buttons.buttons.collection
            """
            return self._config_sub_data('collection', self.Collection)

        @property
        def button(self):
            """
            This option controls the HTML tag that is used to create each individual button.
            With this option the tag type and class name can be specified using the tag and className properties of this
            object.

            Related Pages:

              https://datatables.net/reference/option/buttons.buttons.button
            """
            return self._config_sub_data('button', self.DomButton)

    @property
    def enabled(self):
        """
        This option provides the ability to set the initial enabled state of a button using a boolean value.

        It is most likely to be of use when using the API methods that can control the button's enabled state after
        initialisation:

        Related Pages:

          https://datatables.net/reference/option/buttons.buttons.enabled
        """
        return self._config_get()

    @enabled.setter
    def enabled(self, val):
        self._config(val)

    @property
    def buttons(self) -> InnerButtons:
        """ """
        return self._config_sub_data_enum('buttons', InnerButtons)

    @property
    def dom(self):
        return self._config_sub_data('dom', self.Dom)

    @property
    def name(self):
        """
        Set a name for the instance for the group selector.

        Related Pages:

          https://datatables.net/reference/option/buttons.name
        """
        return self._config_get()

    @name.setter
    def name(self, val):
        self._config(val)
