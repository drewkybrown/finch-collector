from django.shortcuts import render

finches = [
    {
        "name": "Lolo",
        "species": "House Finch",
        "description": "Small, brown, and commonly found in urban areas.",
        "age": 3,
    },
    {
        "name": "Sachi",
        "species": "Zebra Finch",
        "description": "Small, striped finch known for its cheerful singing.",
        "age": 2,
    },
    {
        "name": "Charlie",
        "species": "Goldfinch",
        "description": "Bright yellow plumage during breeding season.",
        "age": 1,
    },
    {
        "name": "Kiwi",
        "species": "Gouldian Finch",
        "description": "Colorful finch with distinct red, black, and green head.",
        "age": 4,
    },
]


# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# Add new view
def finches_index(request):
    return render(request, "finches/index.html", {"finches": finches})
