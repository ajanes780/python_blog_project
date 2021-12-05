from django.shortcuts import render
from datetime import date
posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 3, 27),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 3, 27),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 3, 27),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 3, 27),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 3, 27),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
]


def index(req):

    return render(req, "blog/index.html")


def posts(req):
    return render(req, "blog/all-posts.html")


def post_detail(req, slug):
    return render(req, "blog/post-detail-page.html", )
