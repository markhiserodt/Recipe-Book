import { HttpClient } from '@angular/common/http';
import { Inject, Injectable, inject, signal } from '@angular/core';
import { RecipeRequest } from '../../models/recipe-request.model';
import { Observable, take } from 'rxjs';
import { Recipe } from '../../models/recipe.model';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  private http = inject(HttpClient);

  readonly recipes = signal<Recipe[]>([]);

  constructor(@Inject('BASE_URL') private baseUrl: string) {
    this.getRecipes();
  }

  addRecipe(recipeRequest: RecipeRequest): Observable<any> {
    return this.http.post<any>(`${this.baseUrl + 'api/recipe'}`, recipeRequest);
  }

  getRecipes(): void {
    if (this.recipes().length > 0) return;
    this.http.get<Recipe[]>(`${this.baseUrl + 'api/recipe'}`).pipe(take(1)).subscribe({
      next: (recipes: Recipe[]) => {
        this.recipes.set(recipes);
      }
    });
  }

  updateRecipe(recipeRequest: RecipeRequest): Observable<any> {
    return this.http.put<any>(`${this.baseUrl + 'api/recipe'}`, recipeRequest);
  }

  deleteRecipe(id: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl + 'api/recipe/' + id}`);
  }
}
