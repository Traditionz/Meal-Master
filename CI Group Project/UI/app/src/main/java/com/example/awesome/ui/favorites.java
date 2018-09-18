package com.example.awesome.ui;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;

public class favorites extends AppCompatActivity {
    ArrayList<String> favsNames = new ArrayList<String>();
    ArrayAdapter<String> favsAd;
    private ListView favs;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favorites);
        favsAd = new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1, favsNames);
        favs = (ListView)findViewById(R.id.recList);
        favs.setAdapter(favsAd);
        for(Dish d : resultsPage.dishes){
            if(resultsPage.favorites.contains(d.getKey())){
                favsAd.add(d.getKey());
                favsAd.notifyDataSetChanged();
            }
        }
        favs.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> adapterView, View view, int i, long l) {
                favsNames.remove(i);
                favsAd.notifyDataSetChanged();
                resultsPage.favorites.remove(i);
                return true;
            }
        });
        favs.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                resultsPage.passKey = favsNames.get(i);
                Intent in=new Intent(
                        favorites.this,
                        dishContent.class);
                startActivity(in);
            }
        });
    }
}
