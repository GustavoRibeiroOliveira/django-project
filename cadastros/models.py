from django.db import models


# Cidade.objects.filter(estado__pais__nome='Brasil')
# retorna a cidade do estado quem pertence ao Brasil

# mg = Estado.objects.get(nome='Minas Gerais') -> pega o objeto estado que tem o nome Minas Gerais
# mg.cidade_set.all() -> mostra todas as cidades que pertencer aquele estado

# Cidade.objects.filter(nome__icontains='a')


class Pais(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True,
                               blank=False)  # nulo no banco e não nulo no formulario
    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False, help_text="Marcar se a cidade for capital")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome
