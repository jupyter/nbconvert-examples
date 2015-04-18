{%- extends 'display_priority.tpl' -%}


{% block header %}"""
{% endblock %}

{% block footer %}"""
{% endblock %}

{% block input %}{{ cell.input | prepend_prompt }}
{% endblock input %}

{% block traceback_line %}{{ line | strip_ansi }}
{% endblock traceback_line %}

{% block pyout %}{% block data_priority scoped %}{{ super() }}{% endblock %}{% endblock pyout %}

{% block data_text scoped %}{{ output.text }}
{% endblock data_text %}

{% block stream %}{{ output.text }}{% endblock stream %}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}

{% block headingcell scoped %}
{{ ("#" * cell.level + cell.source) | replace('\n', ' ') }}
{% endblock headingcell %}

{% block unknowncell scoped %}
# unknown type  {{cell.type}}
{% endblock unknowncell %}