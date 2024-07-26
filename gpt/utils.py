import base64
import requests
from users_media.models import Images


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def ask_gpt_about_profile(
    api_key: str, user_images: list[Images], username: str
) -> dict[str, str]:
    promt = f"""
    there is {len(user_images)} images giving to you; i want you to select one of this images based on this parameters:

    1. this image will use in a online chatting platform as a profile
    2. the user username is {username}
    3. if you don't undrestand user username or it do not have meaning only user parameter 1



    and tell me your reason like this:

    [Only the image number based on images order, like: image: 5]

    reason: [Your reason]
    """

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    content_payload = [{"type": "text", "text": promt}]

    for image in user_images:
        encoded_image = encode_image(image.image.path)
        content_payload.append(
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"},
            }
        )

    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": content_payload}],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    # Note: if you asking me its better to parse answer using regex
    # but no time for regex rn

    print(response.json())
    print(response.status_code)
    response = response.json()["choices"][0]["message"]["content"].split("\n\n")
    selected_image = response[0][7:]
    select_reason = response[1][8:]

    return {"image": int(selected_image), "reason": select_reason}
