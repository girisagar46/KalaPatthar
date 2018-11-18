from django.db import models


class Website(models.Model):
    website_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.website_name} {self.title}"


class BlogData(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    website = models.ForeignKey(Website, on_delete=models.DO_NOTHING)
    body = models.TextField()
    images_srcs = models.TextField()
    anchor_links = models.TextField()
    anchor_texts = models.TextField()

    @property
    def to_dict(self):
        data = {
            "website": self.website.id,
            "body": self.body,
            "images_src": self.images_srcs,
            "anchor_links": self.anchor_links,
            "anchor_text": self.anchor_texts,
        }
        return data

    def __str__(self):
        return f"{self.website.website_name} {self.website.title}"
