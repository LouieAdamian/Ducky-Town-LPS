#include <vector>
#include <stdio.h>

#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>
using namespace std;
//using namespace cv;

class Tagger {
  private:
    /* data */

  public:
    cv:Mat makeTag(int id, ){
    cv::aruco::Dictionary dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);

      Mat output(8, 8, DataType<float>::type);
      cv::aruco::drawMarker(dictionary, 23, 200, markerImage, 1);
    }
    Tagger (arguments);
    virtual ~Tagger ();
};
