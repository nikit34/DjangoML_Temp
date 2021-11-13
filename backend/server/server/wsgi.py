import inspect
import os

from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.registry import MLRegistry
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


try:
    registry = MLRegistry()
    rf = RandomForestClassifier()
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))