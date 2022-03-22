__all__ = [
    'NoisyBradleyTerry',
]
import crowdkit.aggregation.base
import pandas


class NoisyBradleyTerry(crowdkit.aggregation.base.BasePairwiseAggregator):
    """A modification of Bradley-Terry with parameters for workers' skills and
    their biases.
    Attributes:
        scores_ (Series): 'Labels' scores.
            A pandas.Series index by labels and holding corresponding label's scores
        skills_ (Series): workers' skills.
            A pandas.Series index by workers and holding corresponding worker's skill
        biases_ (Series): Predicted biases for each worker. Indicates the probability of a worker to choose the left item..
            A series of workers' biases indexed by workers
    """

    def fit(self, data: pandas.DataFrame) -> 'NoisyBradleyTerry':
        """Args:
            data (DataFrame): Workers' pairwise comparison results.
                A pandas.DataFrame containing `worker`, `left`, `right`, and `label` columns'.
                For each row `label` must be equal to either `left` column or `right` column.

        Returns:
            NoisyBradleyTerry: self.
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

    def __init__(
        self,
        n_iter: int = 100,
        tol: float = 1e-05,
        random_state: int = 0
    ) -> None:
        """Method generated by attrs for class NoisyBradleyTerry.
        """
        ...

    scores_: pandas.Series
    n_iter: int
    tol: float
    random_state: int
    skills_: pandas.Series
    biases_: pandas.Series