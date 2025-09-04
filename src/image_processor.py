import numpy as np
import numpy.typing as npt


class ImageProcessor:
    @classmethod
    def crop_to_same_size(cls, images: list[npt.NDArray[np.int_]]) -> npt.NDArray[np.int_]:
        """_summary_

        Parameters
        ----------
        images : list[npt.NDArray[np.int_]]
            _description_

        Returns
        -------
        npt.NDArray[np.int_]
            _description_
        """
        sizes = np.array([image.shape for image in images])
        min_num_rows = np.array(sizes[:, 0]).min()
        min_col_sizes = np.array(sizes[:, 1]).min()

        return np.zeros(3, dtype=int)
