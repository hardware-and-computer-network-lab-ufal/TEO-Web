from django.template import Library

register = Library()

@register.inclusion_tag('templatetags/menu-lateral.html')
def permissao(user):
    permissao_clinica = user.has_perm('brain.add_clinica')
    permissao_profissional = user.has_perm('brain.add_profissional')
    permissao_paciente = user.has_perm('brain.add_paciente')

    context = {
        'permissao_clinica': permissao_clinica,
        'permissao_profissional': permissao_profissional,
        'permissao_paciente': permissao_paciente,
    }

    return context
