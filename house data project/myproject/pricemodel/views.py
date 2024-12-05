from lib2to3.fixes.fix_input import context

from django.shortcuts import render
import os
import numpy as np
import joblib as jb
from . forms import PricePredictionForm


# Create your views here.

def predict_price(request):
    if request.method == 'POST':
        form = PricePredictionForm(request.POST)
        if form.is_valid():
            # load the trained linear regression model
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'linear_regression_model.pkl')
            model = jb.load(model_path)

            # extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)

            # perform prediction
            predicted_price = model.predict(new_data)[0]

            # prepare the response
            context = {
                'form': form,
                'predicted_price': round(predicted_price, 2),
            }
            return render(request, 'pricemodel/index.html', context)
        else:
            form = PricePredictionForm()

        context = {'form': form}
        return render(request, 'pricemodel/index.html', context)