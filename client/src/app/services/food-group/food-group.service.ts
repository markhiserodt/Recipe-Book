import { HttpClient } from '@angular/common/http';
import { Inject, Injectable, inject, signal } from '@angular/core';
import { FoodGroupRequest } from '../../models/food-group-request.model';
import { Observable, take } from 'rxjs';
import { FoodGroup } from '../../models/food-group.model';

@Injectable({
  providedIn: 'root'
})
export class FoodGroupService {
  private http = inject(HttpClient);

  readonly foodGroups = signal<FoodGroup[]>([]);

  constructor(@Inject('BASE_URL') private baseUrl: string) {
    this.getFoodGroups();
  }

  addFoodGroup(foodGroupRequest: FoodGroupRequest): Observable<any> {
    return this.http.post<any>(`${this.baseUrl + 'api/foodGroup'}`, foodGroupRequest);
  }

  getFoodGroups(): void {
    if (this.foodGroups().length > 0) return;
    this.http.get<FoodGroup[]>(`${this.baseUrl + 'api/foodGroup'}`).pipe(take(1)).subscribe({
      next: (foodGroups: FoodGroup[]) => {
        this.foodGroups.set(foodGroups);
      }
    });
  }

  // getFoodGroups(): Observable<FoodGroup[]> {
  //   return this.http.get<FoodGroup[]>(`${this.baseUrl + 'api/foodGroup'}`);
  // }

  updateFoodGroup(foodGroupRequest: FoodGroupRequest): Observable<any> {
    return this.http.put<any>(`${this.baseUrl + 'api/foodGroup'}`, foodGroupRequest);
  }

  deleteFoodGroup(id: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl + 'api/foodGroup/' + id}`);
  }
}
