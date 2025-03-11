"""
Main application script for running the ML model service.

This script initializes the ModelService, loads the ML model, makes
a prediction based on predefined input parameters, and logs teh output.
It demonstrates the typical workflow of using the ModelService in
a practical application context.
"""

from loguru import logger

from model.model_builder import ModelBuilderService


@logger.catch
def main():
    """
    Run the application.

    load the model, make a prediction based on provided data,
    """
    logger.info("running the aplication")
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == "__main__":
    main()
