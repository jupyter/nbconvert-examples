{%- extends 'html_basic.tpl' -%}

<b>Cell</b>
{%- block markdowncell -%}
    <br><br>
    {{super()}}
{%- endblock markdowncell -%}

{%- block headingcell -%}
{%- endblock headingcell -%}
{%- block rawcell -%}
{%- endblock rawcell -%}
{%- block unknowncell -%}
{%- endblock unknowncell -%}
{%- block codecell -%}
{%- endblock codecell -%}
