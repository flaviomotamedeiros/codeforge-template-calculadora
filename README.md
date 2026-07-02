# Calculadora Científica

Implementem em equipe uma calculadora científica completa. Cada membro fica responsável por uma seção de funções.

> 📦 **Template de trabalho em grupo do CodeForge.** Clique em **Use this template** → **Create a new repository** para criar o repositório do seu grupo.

## 🚀 Como rodar

```bash
python -m pytest tests/ -v   # rodar os testes
python -c "from calculator import add; print(add(2, 3))"  # testar uma função
```

## 📋 Distribuição de funções por membro

| Seção | Funções | Responsável |
|-------|---------|-------------|
| 1 — Operações básicas | `add`, `subtract`, `multiply`, `divide` | Membro 1 |
| 2 — Potência e raiz | `power`, `sqrt`, `cbrt` | Membro 2 |
| 3 — Trigonometria | `sin`, `cos`, `tan`, `degrees_to_radians`, `radians_to_degrees` | Membro 3 |
| 4 — Logaritmos | `log`, `log10`, `log_base` | Membro 4 |
| 5 — Estatística | `mean`, `median`, `mode`, `std_dev` | Membro 5 |

> Atualize a tabela com os nomes dos membros do grupo.

## 📋 Requisitos

- **Operações básicas** — `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` com tratamento de divisão por zero
- **Potência e raiz** — `power(base, exp)`, `sqrt(n)`, `cbrt(n)` com validação de negativos
- **Trigonometria** — `sin(x)`, `cos(x)`, `tan(x)`, `degrees_to_radians(d)`, `radians_to_degrees(r)`
- **Logaritmos** — `log(x)` (natural), `log10(x)`, `log_base(x, base)` com validação de domínio
- **Estatística** — `mean(values)`, `median(values)`, `mode(values)`, `std_dev(values)`
- Todas as funções devem lançar `ValueError` para entradas inválidas
- Cada função deve ter sua docstring explicando parâmetros e retorno
- O README deve conter a tabela de distribuição de funções por aluno

## 👥 Trabalho em equipe (obrigatório)

- O repositório deve pertencer a **um** dos membros do grupo. Os **demais membros entram como colaboradores** em `Settings → Collaborators → Add people`.
- Cada membro trabalha em sua **própria branch** e abre **Pull Request** para a `main`, pedindo revisão de outro colega.
- O CodeForge mede as **contribuições individuais** de cada membro direto do histórico do GitHub.

## 🧱 Stack

- Python 3.10+
- Sem dependências externas (apenas biblioteca padrão)
