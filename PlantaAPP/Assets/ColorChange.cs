using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ColorChange : MonoBehaviour
{
    // Start is called before the first frame update
    //Color day = new Color(0f, 0f, 0f, 0f);
    //Color night = new Color(1f, 1f, 1f, 0.1f);

    public Slider colorSlider;
    Color color;

    void Start()
    {
        color = gameObject.GetComponent<Image>().color;
    }

    // Update is called once per frame
    void Update()
    {
        //Get slider value
        

        //Change the object color
        Color dayNight = new Color(color.r, color.g, color.b, colorSlider.value - 0.2f);
        gameObject.GetComponent<Image>().color = dayNight;
    }

}
