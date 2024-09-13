"""
This is a boilerplate pipeline 'prepare_data'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, node, pipeline

from plant_traits.pipelines.prepare_data.nodes import (
    add_path_to_images,
    split_train_test,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        pipe=[
            node(
                func=add_path_to_images,
                inputs=["df_raw", "params:path_images"],
                outputs="df_w_path",
                name="add_path_to_images"
            ),
            node(
                func=split_train_test,
                inputs="df_w_path",
                outputs=["df_train", "df_valid"],
                name="split_data_train_validation"
            ),
        ],
        inputs="df_raw",
        outputs=["df_train", "df_valid"],
        namespace="prepare_data"
    )
