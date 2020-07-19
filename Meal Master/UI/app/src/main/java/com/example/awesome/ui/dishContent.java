package com.example.awesome.ui;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import com.example.awesome.ui.Dish;

import java.util.ArrayList;

public class dishContent extends AppCompatActivity {
    ArrayList<String> everything = new ArrayList<String>();
    ArrayAdapter<String> ad;
    private ListView content;
    private TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dish_content);
        ad = new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1, everything);
        content = findViewById(R.id.contents);
        content.setAdapter(ad);
        tv = (TextView)findViewById(R.id.textView);

        for(Dish d: resultsPage.dishes){
            if(d.getKey().equals(resultsPage.passKey)){
                tv.setText(resultsPage.passKey);
                everything.add("INGREDIENTS");
                ad.notifyDataSetChanged();
                for(String ing: d.getIngredients()){
                    if(ing==null){
                        continue;
                    }
                    everything.add(ing);
                    ad.notifyDataSetChanged();
                }
                everything.add("INSTRUCTIONS");
                ad.notifyDataSetChanged();
                for(String inst: d.getInstructions()){
                    if(inst==null){
                        continue;
                    }
                    everything.add(inst);
                    ad.notifyDataSetChanged();
                }
                everything.add("");
                ad.notifyDataSetChanged();
            }
        }
    }

}
