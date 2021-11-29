import csv

from commons import get_model, transform_image

from imgtag.ImgTagDataset import convert_onehot_string_labels

csv_path = "./static/class_name.csv"
CLASS_NAME = None
with open(csv_path, "r") as csvfile:
    CLASS_NAME = [cn for cn in csv.reader(csvfile)][0]

model = get_model(len(CLASS_NAME))


def get_prediction(image_byte):
    try:
        tensor = transform_image(image_byte)
        preds = model.forward(tensor)
    except Exception:
        return 0, 'error'

    pred = preds[0]
    pred[pred > 0.5] = 1
    pred[pred <= 0.5] = 0

    labels = convert_onehot_string_labels(CLASS_NAME, pred.detach().numpy())

    return labels
