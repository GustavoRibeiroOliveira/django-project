from rest_framework import serializers

from tickets.models import Solicitacao, Interacao


class InteracaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interacao
        fields = '__all__'


class SolicitacaoSerializer(serializers.ModelSerializer):

    interacoes = InteracaoSerializer(many=True, read_only=True)
    # nesse caso n precisa do source porque o related_name do model ja é o nome da variavel ('interacoes')
    # interacoes = InteracaoSerializer(many=True, read_only=True, source='interacao_set')

    class Meta:
        model = Solicitacao
        fields = ['id', 'categoria', 'nome', 'email', 'assunto', 'descricao', 'arquivo', 'status', 'atendente',
                  'data_solicitacao', 'ultima_atualizacao', 'interacoes']
