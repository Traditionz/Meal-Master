package com.example.awesome.ui;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.math.RoundingMode;
import java.util.ArrayList;

public class resultsPage extends AppCompatActivity {
    public static ArrayList<Dish> dishes = new ArrayList<>();
    ArrayList<String> rpsNames = new ArrayList<String>();
    ArrayAdapter<String> adapt;
    public static String passKey;
    public static ArrayList<String> favorites = new ArrayList<String>();
    private ListView rList;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_results_page);
        final FirebaseDatabase Recipes = FirebaseDatabase.getInstance();

        adapt = new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1, rpsNames);
        rList = (ListView) findViewById(R.id.recipeList);
        rList.setAdapter(adapt);
        DatabaseReference ref = Recipes.getReference("RECIPES");
        ref.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                dishes.clear();
                for(DataSnapshot rSnap: dataSnapshot.getChildren()){
                    Dish dish = rSnap.getValue(Dish.class);
                    dishes.add(dish);
                    //System.out.println(dish.getKey());
                    dish.setKey(rSnap.getKey());
                    System.out.println(dish.getKey());
                    System.out.println(dish.getTaglines());
                    System.out.println(dish.getIngredients());
                    System.out.println(dish.getInstructions());

                }
                getRecipeNames();
                rList.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
                    @Override
                    public boolean onItemLongClick(AdapterView<?> adapterView, View view, int i, long l) {
                        String name = rpsNames.get(i);
                        String[] split = name.split("\n");
                        favorites.add(split[0]);
                        return true;
                    }
                });
                rList.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                        String name = rpsNames.get(i);
                        String[] split = name.split("\n");
                        passKey = split[0];
                        Intent in=new Intent(
                                resultsPage.this,
                                dishContent.class);
                        startActivity(in);
                    }
                });
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {



            }
        });



    }
    public void getRecipeNames(){
        double count = 0.0;
        double match = 0.0;
        double percent = 0.0;
        System.out.println(rpsNames);
        for(Dish recipe: dishes){
            for(String ing: recipe.getTaglines()){
                if(ing==null){
                    continue;
                }
                else if(MainActivity.list.contains(ing.toLowerCase())){
                    System.out.println(ing);
                    match++;
                    count++;
                }
                else{
                    count++;
                }

            }
            System.out.println(match);
            System.out.println(count);
            System.out.println(MainActivity.list);
            System.out.println(match/count);
            System.out.println(recipe.getKey());
            if((match/count)>(.4)){
                percent = round((match/count)*100,2);
                rpsNames.add(recipe.getKey()+"\nMatch Percentage " + '%'+Double.toString(percent));
                adapt.notifyDataSetChanged();
                match = 0.0;
                count = 0.0;
                System.out.println("ADDED HERREEEE!!!!!!!");


            }
            else{
                match = 0.0;
                count = 0.0;

            }

        }

    }
    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        long factor = (long) Math.pow(10, places);
        value = value * factor;
        long tmp = Math.round(value);
        return (double) tmp / factor;
    }



}
