import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import User

# Dados dos usuários
users_data = [
    {
        'name': 'João Silva',
        'email': 'joao@example.com',
        'phone': '(11) 98765-4321',
        'address': 'Rua A, 123 - São Paulo, SP',
        'is_active': True,
    },
    {
        'name': 'Maria Santos',
        'email': 'maria@example.com',
        'phone': '(11) 99876-5432',
        'address': 'Avenida B, 456 - São Paulo, SP',
        'is_active': True,
    },
    {
        'name': 'Pedro Oliveira',
        'email': 'pedro@example.com',
        'phone': '(21) 98765-4321',
        'address': 'Rua C, 789 - Rio de Janeiro, RJ',
        'is_active': True,
    },
    {
        'name': 'Ana Costa',
        'email': 'ana@example.com',
        'phone': '(21) 99876-5432',
        'address': 'Avenida D, 321 - Rio de Janeiro, RJ',
        'is_active': True,
    },
    {
        'name': 'Carlos Ferreira',
        'email': 'carlos@example.com',
        'phone': '(31) 98765-4321',
        'address': 'Rua E, 654 - Belo Horizonte, MG',
        'is_active': True,
    },
    {
        'name': 'Fernanda Gomes',
        'email': 'fernanda@example.com',
        'phone': '(31) 99876-5432',
        'address': 'Avenida F, 987 - Belo Horizonte, MG',
        'is_active': True,
    },
    {
        'name': 'Lucas Martins',
        'email': 'lucas@example.com',
        'phone': '(41) 98765-4321',
        'address': 'Rua G, 111 - Curitiba, PR',
        'is_active': True,
    },
    {
        'name': 'Patricia Rocha',
        'email': 'patricia@example.com',
        'phone': '(41) 99876-5432',
        'address': 'Avenida H, 222 - Curitiba, PR',
        'is_active': True,
    },
    {
        'name': 'Roberto Lima',
        'email': 'roberto@example.com',
        'phone': '(51) 98765-4321',
        'address': 'Rua I, 333 - Porto Alegre, RS',
        'is_active': True,
    },
    {
        'name': 'Juliana Alves',
        'email': 'juliana@example.com',
        'phone': '(51) 99876-5432',
        'address': 'Avenida J, 444 - Porto Alegre, RS',
        'is_active': True,
    },
    {
        'name': 'Marcelo Pereira',
        'email': 'marcelo@example.com',
        'phone': '(61) 98765-4321',
        'address': 'Quadra K, 555 - Brasília, DF',
        'is_active': True,
    },
    {
        'name': 'Beatriz Nunes',
        'email': 'beatriz@example.com',
        'phone': '(61) 99876-5432',
        'address': 'Quadra L, 666 - Brasília, DF',
        'is_active': True,
    },
]

# Criar usuários
created = 0
for user_data in users_data:
    user, created_flag = User.objects.get_or_create(
        email=user_data['email'],
        defaults={
            'name': user_data['name'],
            'phone': user_data['phone'],
            'address': user_data['address'],
            'is_active': user_data['is_active'],
        }
    )
    if created_flag:
        created += 1
        print(f'✓ Criado: {user.name}')
    else:
        print(f'✗ Já existe: {user.name}')

print(f'\n{created} novos usuários adicionados!')
