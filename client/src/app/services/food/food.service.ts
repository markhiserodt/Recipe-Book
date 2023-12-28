import { HttpClient } from '@angular/common/http';
import { Inject, Injectable, inject, signal } from '@angular/core';
import { Observable, take } from 'rxjs';
import { FoodGroupRequest } from '../../models/food-group-request.model';
import { FoodRequest } from '../../models/food-request.model';
import { Food } from '../../models/food.model';

@Injectable({
  providedIn: 'root'
})
export class FoodService {
  private http = inject(HttpClient);

  readonly foods = signal<Food[]>([]);

  constructor(@Inject('BASE_URL') private baseUrl: string) {
    this.getFoods();
  }

  addFood(foodRequest: FoodRequest): Observable<any> {
    return this.http.post<any>(`${this.baseUrl + 'api/food'}`, foodRequest);
  }

  getFoods(): void {
    if (this.foods().length > 0) return;
    this.http.get<Food[]>(`${this.baseUrl + 'api/food'}`).pipe(take(1)).subscribe({
      next: (foods: Food[]) => {
        this.foods.set(foods);
      }
    });
  }

  updateFood(foodRequest: FoodRequest): Observable<any> {
    return this.http.put<any>(`${this.baseUrl + 'api/food'}`, foodRequest);
  }

  deleteFood(id: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl + 'api/food/' + id}`);
  }
}
