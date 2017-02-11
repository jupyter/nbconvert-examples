{%- extends 'null.tpl' -%}

{% block header %}
%% Exported from Jupyter Notebook
{% endblock header %}

{% block in_prompt %}
%% Cell[{{ cell.execution_count if cell.execution_count else ' ' }}]:
{% endblock in_prompt %}

{% block input %}
{{ cell.source }}
{% endblock input %}

{% block markdowncell scoped %}
%%
{{ cell.source | comment_lines(prefix='% ') }}
{% endblock markdowncell %}
