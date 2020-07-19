package com.example.awesome.ui;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class startScreen extends AppCompatActivity implements View.OnClickListener{
    private Button fav;
    private Button ser;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start_screen);
        ser = (Button)findViewById(R.id.goSearch);
        ser.setOnClickListener(this);
        fav = (Button)findViewById(R.id.goFavorites);
        fav.setOnClickListener(this);
    }
    public void onClick(View v)
    {
        if(v.getId() == R.id.goSearch){
            Intent intent = new Intent(startScreen.this, MainActivity.class);
            startActivity(intent);

        }else if(v.getId() == R.id.goFavorites){
            Intent intent = new Intent(startScreen.this, favorites.class);
            startActivity(intent);
        }

    }
}

