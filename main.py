from mongoengine import connect, errors, NotUniqueError, ValidationError, MultipleObjectsReturned, DoesNotExist
from config import DB_NAME, HOST, PORT
from model.posts import Post


connect(
    db=DB_NAME,
    host=HOST,
    port=PORT
)

try:
    # create and save post
    # post = Post(
    #     title="Build your first chatbot",
    #     description="Lorem ipsum dolor sit amet....",
    #     status="ACTIVE"
    # )

    # result = post.save()

    # print("Post with title:: {}, has been saved".format(result.title))

    # fetch all posts from the Post collection
    # saved_posts = Post.objects()
    # for post in saved_posts:
    #     print(post.title)

    # fetch a specific document from the database
    # single_object = Post.objects(title="Build your first chatbot").get()
    # print("Single object {}".format(single_object.description))

    # fetch the first document
    # result = Post.objects(description="Lorem ipsum dolor sit amet....").first()
    # print("first object details:: {}".format(result.date_created))

    # fetch and update a document
    post = Post.objects(title="My First Java Program").get()
    result = post.update(
        title="My First Python Program",
        description="In this post, I will teach you how to build your first Python application."
    )

    # call .reload() on the query object in order to access the updated data
    post.reload()
    print("update result:: {}".format(result))
    print("new title:: {}".format(post.title))



except ValidationError as valerr:
    print("Validation error {}".format(str(valerr)))
except NotUniqueError as notunique:
    print("Field not unique error {}".format(str(notunique)))
except MultipleObjectsReturned as multiobjectreturned:
    print("Multiple objects returned error {}".format(str(multiobjectreturned)))
except DoesNotExist as doesnotexsit:
    print("Object does not exist error {}".format(str(doesnotexsit)))
