from rest_framework import serializers
from users.models import Cuenta, CuentaPerfil


class CuentaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Cuenta (usuario custom)
    """
    email = serializers.EmailField(required=True)
    usuario = serializers.CharField(required=False)
    clave = serializers.CharField(min_length=8, write_only=True)
    confirmar_clave = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Cuenta
        fields = ('email', 'usuario', 'clave', 'confirmar_clave')
        extra_kwargs = {'clave': {'write_only': True}, 'confirmar_clave': {'write_only': True}}

    def validate(self, data):
        """
        Verifies password and confirm_password are the same.
        """
        if data.get('clave') != data.get('confirmar_clave'):
            raise serializers.ValidationError({"confirmar_clave": "Las contraseñas no son iguales."})
        return data

    def create(self, validated_data):
        """
        Set the validated password and other data and return a new `Account` instance.
        :param validated_data:
        :return: instance of Account
        """
        validated_data.pop('confirmar_clave')
        clave = validated_data.pop('clave', None)

        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if clave is not None:
            instance.set_password(clave)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        clave = validated_data.pop('clave', None)
        instance = super().update(instance, validated_data)
        if clave:
            instance.set_password(clave)
            instance.save()
        return instance


class CuentaPerfilSerializer(serializers.ModelSerializer):
    """
    Serializer for Account profile model
    """
    nombre = serializers.CharField(max_length=150, required=True)
    apellido = serializers.CharField(max_length=150, required=True)
    telefono = serializers.CharField(required=False, allow_blank=True)
    descripcion = serializers.CharField(required=False, allow_blank=True)
    cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.filter(eliminado=False))

    class Meta:
        model = CuentaPerfil
        fields = ('nombre', 'apellido', 'telefono', 'descripcion', 'cuenta')

        # Create function is the default


# ----------- PASSWORD RESET -----------
class SoliciarReestablecerClaveSerializer(serializers.Serializer):
    """
    Serializer for password reset request
    """
    email = serializers.EmailField(required=True)


class ReestablecerClaveSerializer(serializers.ModelSerializer):
    """
    Validate password reset
    """
    clave = serializers.CharField(min_length=8, write_only=True, required=True)
    confirmar_clave = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = Cuenta
        fields = ('clave', 'confirmar_clave')
        extra_kwargs = {'clave': {'write_only': True}, 'confirmar_clave': {'write_only': True}}

    def validate(self, data):
        """
        Verifies password and confirm_password are the same.
        """
        if data.get('clave') != data.get('confirmar_clave'):
            raise serializers.ValidationError({"confirmar_clave": "Las contraseñas no son iguales."}) # if passwords don't match, raise Exception

        return data

    def update(self, instance, validated_data):
        """
        Updates the user's password
        """
        instance.set_password(validated_data['clave'])  # Encrypts the password
        instance.save()

        return instance
