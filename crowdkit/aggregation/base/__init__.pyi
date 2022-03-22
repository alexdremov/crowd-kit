__all__ = [
    'BaseClassificationAggregator',
    'BaseImageSegmentationAggregator',
    'BaseEmbeddingsAggregator',
    'BaseTextsAggregator',
    'BasePairwiseAggregator',
]
import pandas
import typing


class BaseClassificationAggregator:
    """This is a base class for all classification aggregators
    Attributes:
        labels_ (typing.Optional[pandas.core.series.Series]): Tasks' labels.
            A pandas.Series indexed by `task` such that `labels.loc[task]`
            is the tasks's most likely true label.
    """

    def fit(self, data: pandas.DataFrame) -> 'BaseClassificationAggregator':
        """Args:
            data (DataFrame): Workers' labeling results.
                A pandas.DataFrame containing `task`, `worker` and `label` columns.
        Returns:
            BaseClassificationAggregator: self.
        """
        ...

    def fit_predict(self, data: pandas.DataFrame) -> pandas.Series:
        """Args:
            data (DataFrame): Workers' labeling results.
                A pandas.DataFrame containing `task`, `worker` and `label` columns.
        Returns:
            Series: Tasks' labels.
                A pandas.Series indexed by `task` such that `labels.loc[task]`
                is the tasks's most likely true label.
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseClassificationAggregator.
        """
        ...

    labels_: typing.Optional[pandas.Series]


class BaseImageSegmentationAggregator:
    """This is a base class for all image segmentation aggregators
    Attributes:
        segmentations_ (Series): Tasks' segmentations.
            A pandas.Series indexed by `task` such that `labels.loc[task]`
            is the tasks's aggregated segmentation.
    """

    def fit(self, data: pandas.DataFrame) -> 'BaseImageSegmentationAggregator':
        """Args:
            data (DataFrame): Workers' segmentations.
                A pandas.DataFrame containing `worker`, `task` and `segmentation` columns'.

        Returns:
            BaseImageSegmentationAggregator: self.
        """
        ...

    def fit_predict(self, data: pandas.DataFrame) -> pandas.Series:
        """Args:
            data (DataFrame): Workers' segmentations.
                A pandas.DataFrame containing `worker`, `task` and `segmentation` columns'.

        Returns:
            Series: Tasks' segmentations.
                A pandas.Series indexed by `task` such that `labels.loc[task]`
                is the tasks's aggregated segmentation.
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseImageSegmentationAggregator.
        """
        ...

    segmentations_: pandas.Series


class BaseEmbeddingsAggregator:
    """This is a base class for all embeddings aggregators
    Attributes:
        embeddings_and_outputs_ (DataFrame): Tasks' embeddings and outputs.
            A pandas.DataFrame indexed by `task` with `embedding` and `output` columns.
    """

    def fit(self, data: pandas.DataFrame) -> 'BaseEmbeddingsAggregator':
        """Args:
            data (DataFrame): Workers' outputs with their embeddings.
                A pandas.DataFrame containing `task`, `worker`, `output` and `embedding` columns.
        Returns:
            BaseEmbeddingsAggregator: self.
        """
        ...

    def fit_predict(self, data: pandas.DataFrame) -> pandas.DataFrame:
        """Args:
            data (DataFrame): Workers' outputs with their embeddings.
                A pandas.DataFrame containing `task`, `worker`, `output` and `embedding` columns.
        Returns:
            DataFrame: Tasks' embeddings and outputs.
                A pandas.DataFrame indexed by `task` with `embedding` and `output` columns.
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseEmbeddingsAggregator.
        """
        ...

    embeddings_and_outputs_: pandas.DataFrame


class BaseTextsAggregator:
    """This is a base class for all texts aggregators
    Attributes:
        texts_ (Series): Tasks' texts.
            A pandas.Series indexed by `task` such that `result.loc[task, text]`
            is the task's text.
    """

    def fit(self, data: pandas.DataFrame) -> 'BaseTextsAggregator':
        """Args:
            data (DataFrame): Workers' text outputs.
                A pandas.DataFrame containing `task`, `worker` and `text` columns.
        Returns:
            BaseTextsAggregator: self.
        """
        ...

    def fit_predict(self, data: pandas.DataFrame) -> pandas.Series:
        """Args:
            data (DataFrame): Workers' text outputs.
                A pandas.DataFrame containing `task`, `worker` and `text` columns.
        Returns:
            Series: Tasks' texts.
                A pandas.Series indexed by `task` such that `result.loc[task, text]`
                is the task's text.
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseTextsAggregator.
        """
        ...

    texts_: pandas.Series


class BasePairwiseAggregator:
    """This is a base class for all pairwise comparison aggregators
    Attributes:
        scores_ (Series): 'Labels' scores.
            A pandas.Series index by labels and holding corresponding label's scores
    """

    def fit(self, data: pandas.DataFrame) -> 'BasePairwiseAggregator':
        """Args:
            data (DataFrame): Workers' pairwise comparison results.
                A pandas.DataFrame containing `worker`, `left`, `right`, and `label` columns'.
                For each row `label` must be equal to either `left` column or `right` column.

        Returns:
            BasePairwiseAggregator: self.
        """
        ...

    def fit_predict(self, data: pandas.DataFrame) -> pandas.Series:
        """Args:
            data (DataFrame): Workers' pairwise comparison results.
                A pandas.DataFrame containing `worker`, `left`, `right`, and `label` columns'.
                For each row `label` must be equal to either `left` column or `right` column.

        Returns:
            Series: 'Labels' scores.
                A pandas.Series index by labels and holding corresponding label's scores
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class BasePairwiseAggregator.
        """
        ...

    scores_: pandas.Series