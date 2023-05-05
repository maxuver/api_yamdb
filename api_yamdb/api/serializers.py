from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
from users.validators import validate_username


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[validate_username,
                    UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254, validators=[
            UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')


class CreateUserSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z', required=True, max_length=150)
    email = serializers.EmailField(required=True, max_length=254)

    '''class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email'])
        ]'''

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(
                (f'{value} служебное имя!')
            )
        return value

    '''def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists:
            raise serializers.ValidationError(f'{email} уже существует!')'''

    '''def validate(self, data):
        email = data['email']
        username = data['username']
        if (User.objects.filter(email=email).exists
           and User.objects.get(email=email).username != username):
            raise serializers.ValidationError(f'{email} уже существует!')
        if (User.objects.filter(username=username).exists
           and User.objects.get(username=username).email != email):
            raise serializers.ValidationError(f'{username} уже существует!')
        return data'''


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
    rating = serializers.IntegerField()

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


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(default=serializers.
                                          CurrentUserDefault(),
                                          slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class CommentListSerializer(serializers.ModelSerializer):
    results = CommentSerializer(many=True)

    class Meta:
        fields = ('count', 'next', 'previous', 'results')
        model = Comment
