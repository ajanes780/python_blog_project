from django.shortcuts import render
from datetime import date
all_posts = [
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
        "title": "Bike race",
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
        "title": " Race Car",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "woods.jpg",
        "author": "Aaron Janes",
        "date": date(2021, 4, 27),
        "title": "Kayak",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut? Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui. Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
    {
        "slug": "coding",
        "image": "coding.jpeg",
        "author": "Aaron Janes",
        "date": date(2021, 7, 27),
        "title": "CODING",
        "excerpt": "There is nothing like the the views in the mountain i wasn't even prepared for what happened next",
        "content": """
        Lorem ipsum dolor it amet consectetur adipisicing elit. Distinctio perferendis voluptatum iure numquam quia autem dolore at expedita officia harum odio minus consequatur nisi ipsam quasi aut, eum natus voluptate earum obcaecati molestiae ea ut?
        
        Numquam optio voluptates enim veniam vitae nesciunt nam explicabo ab suscipit, quos molestias, amet nisi nobis ducimus magni inventore quisquam dolorum quia? Similique ut optio, officia iste nulla natus a id numquam repudiandae voluptates autem suscipit iure molestias possimus delectus corrupti quod ad non qui.
        
        Repellat ratione impedit sapiente placeat illo voluptatum eveniet dolor ipsum iste cupiditate molestiae, dolores porro aspernatur sint quis id assumenda?
        """
    },
]


def get_date(post):
    return post["date"]


def index(req):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(req, "blog/index.html", {
        "posts": latest_post
    })


def posts(req):
    return render(req, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(req, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(req, "blog/post-detail-page.html", {"post":identified_post})
