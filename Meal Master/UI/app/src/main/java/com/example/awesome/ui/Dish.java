package com.example.awesome.ui;

import android.nfc.Tag;
import android.util.Log;

import java.util.ArrayList;

/**
 * Created by torin on 4/26/2018.
 */

public class Dish {
    ArrayList<String> Taglines;
    ArrayList<String> Instructions;
    ArrayList<String> Ingredients;
    String Key;
    public String getKey(){
        return Key;
    }
    public ArrayList<String> getTaglines(){

        return Taglines;
    }
    public ArrayList<String> getInstructions(){

        return Instructions;
    }
    public ArrayList<String> getIngredients(){

        return Ingredients;
    }

    public void setKey(String key){
        Key=key;
    }

    public void setTaglines(ArrayList<String> taglines){
        Taglines=taglines;
    }

    public void setInstructions(ArrayList<String> instructions){
        Instructions=instructions;
    }

    public void setIngredients(ArrayList<String> ingredients){
        Ingredients=ingredients;
    }
}
