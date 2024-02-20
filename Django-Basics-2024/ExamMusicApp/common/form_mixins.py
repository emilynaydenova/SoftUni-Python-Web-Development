class ReadonlyDisabledFieldsMixin:
    readonly_fields = ()
    disabled_fields = ()
    # can make readonly_fields as property and define '__all__' as self.fields.keys()
    def __init__(self):
        self.fields = None

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["readonly"] = True

    def _mark_disabled_fields(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["disabled"] = True

# to apply in views
class ReadonlyViewMixin:
    def get_form(self,form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
