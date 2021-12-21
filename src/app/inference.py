import json

from commons import get_model, transform_image

from imgtag.ImgTagDataset import convert_onehot_string_labels_multi


# json_path = "./static/class_name.json"
json_path = "./static/screw_class_name.json"
json_arr = None
with open(json_path, 'r', encoding='utf-8') as file:
    json_arr = json.load(file)

model = get_model(len(json_arr['English']))


def get_prediction(image_byte):
    try:
        tensor = transform_image(image_byte)
        preds = model.forward(tensor)
    except Exception:
        return 0, 'error'

    pred = preds[0]
    pred[pred > 0.5] = 1
    pred[pred <= 0.5] = 0

    labels = convert_onehot_string_labels_multi(json_arr, pred.detach().numpy())

    return json.loads(labels)
