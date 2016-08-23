# -*- coding: utf-8 -*-

import colander
import deform

from h import i18n
from h.accounts.schemas import CSRFSchema
from h.groups.models import (
    GROUP_DESCRIPTION_MAX_LENGTH,
    GROUP_NAME_MIN_LENGTH,
    GROUP_NAME_MAX_LENGTH,
)


_ = i18n.TranslationString


class GroupSchema(CSRFSchema):

    """The schema for the create-a-new-group form."""

    name = colander.SchemaNode(
        colander.String(),
        title=_("What do you want to call the group?"),
        validator=colander.Length(
            min=GROUP_NAME_MIN_LENGTH,
            max=GROUP_NAME_MAX_LENGTH),
        widget=deform.widget.TextInputWidget(
            autofocus=True,
            css_class="group-form__name-input js-group-name-input",
            disable_autocomplete=True,
            label_css_class="group-form__name-label",
            max_length=GROUP_NAME_MAX_LENGTH,
            placeholder=_("Group Name")))

    description = colander.SchemaNode(
        colander.String(),
        title=_("Description:"),
        validator=colander.Length(max=GROUP_DESCRIPTION_MAX_LENGTH),
        missing=None,
        widget=deform.widget.TextAreaWidget(
            css_class="group-form__description-input",
            label_css_class="group-form__description-label",
            min_length=0,
            max_length=GROUP_DESCRIPTION_MAX_LENGTH,
            placeholder=_("Group Description")))


class LegacyGroupSchema(CSRFSchema):

    """The legacy schema for the create-a-new-group form."""

    name = colander.SchemaNode(
        colander.String(),
        title=_("What do you want to call the group?"),
        validator=colander.Length(
            min=GROUP_NAME_MIN_LENGTH,
            max=GROUP_NAME_MAX_LENGTH),
        widget=deform.widget.TextInputWidget(
            autofocus=True,
            css_class="group-form__name-input js-group-name-input",
            disable_autocomplete=True,
            label_css_class="group-form__name-label",
            max_length=GROUP_NAME_MAX_LENGTH,
            placeholder=_("Group Name")))
