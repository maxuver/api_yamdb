from rest_framework import serializers, validators

from reviews.models import Title, Genre, Category, Review
from users.models import User
from users.validators import validate_username
from rest_framework.validators import UniqueValidator


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[validate_username,
                    UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email')
        model = User

    def validate(self, attrs):
        if len(attrs['username']) > 150:
            raise serializers.ValidationError(
                'Длина имени пользователя не должна превышать 150 символов')
        return attrs


class UserJWTTokenCreateSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[validate_username, ]
    )
    confirmation_code = serializers.CharField(required=True)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        fields = '__all__'
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all())
    genre = serializers.SlugRelatedField(
        many=True, slug_field='slug', queryset=Genre.objects.all())

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(default=serializers.
                                          CurrentUserDefault(),
                                          slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, attrs):
        request = self.context.get('request')
        if request.method == 'POST':
            review = Review.objects.filter(
                author=request.user,
                title=self.context.get('view').kwargs.get('title_id')
            )
            if review:
                raise serializers.ValidationError('Отзыв уже оставлен!')
        return attrs


class ReviewListSerializer(serializers.ModelSerializer):
    results = ReviewSerializer(many=True)

    class Meta:
        fields = ('count', 'next', 'previous', 'results')
        model = Review
